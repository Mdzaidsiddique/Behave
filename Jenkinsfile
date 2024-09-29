pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main', url: 'https://github.com/Mdzaidsiddique/Behave.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    echo Checking Python and Pip versions...
                    python --version
                    pip --version
                    echo Installing dependencies...
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Behave tests
                script {
                    // Change to the directory where your features are located if needed
                    bat 'behave'
                }
            }
        }
    }

    post {
        always {
            // Archive test results or logs, if any
            archiveArtifacts artifacts: 'results/**', fingerprint: true
        }

        success {
            echo 'Tests passed!'
        }

        failure {
            echo 'Tests failed!'
        }
    }
}
