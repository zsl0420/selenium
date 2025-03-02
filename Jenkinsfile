pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // 示例：执行 Maven 构建
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
