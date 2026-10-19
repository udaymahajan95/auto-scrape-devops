pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Tests') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r application/requirements.txt
                    python -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t auto-scrape-devops:${BUILD_NUMBER} .
                '''
            }
        }
    }

    post {
        success {
            echo 'AutoScrape CI pipeline completed successfully!'
        }
        failure {
            echo 'AutoScrape CI pipeline failed. Check the stage logs.'
        }
    }
}
