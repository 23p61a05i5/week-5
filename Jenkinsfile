pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Build stage completed.'
            }
        }

        stage('Run Python Program') {
            steps {
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
