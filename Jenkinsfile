pipeline {
    agent any

    stages {

        stage('Clone from GitHub') {
            steps {
                git 'https://github.com/23p61a05i5/week-5'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage completed.'
            }
        }

        stage('Run Python Program') {
            steps {
                echo 'Running Python program...'
                sh 'python3 calculator.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
