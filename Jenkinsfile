pipeline {
    agent any 

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your GitHub repository
                git 'https://github.com/Mdzaidsiddique/Behave.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python packages using pip
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Behave tests
                bat 'behave'
            }
        }
    }

    post {
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
