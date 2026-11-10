pipeline {
    agent any
    environment {
        IMAGE_NAME = "ex3-converter"
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --rm --user $(id -u):$(id -g) -v $WORKSPACE:/app -w /app $IMAGE_NAME:$IMAGE_TAG pytest --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
        stage('Publish') {
            steps {
                archiveArtifacts artifacts: 'results.xml', fingerprint: true
            }
        }
    }
}
