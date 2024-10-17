pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/bharathcsmys/Jenkins-Test', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install Flask
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 sample.py & disown
                '''
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
    }
}
