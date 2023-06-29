pipeline{
    
    agent any
    
    stages{
        stage('git checkout'){
            steps{
                git credentialsId:'59386c48-d0d6-406c-b4d0-999d84c16bf7',url:'https://github.com/MathisD49/magasin_informatique.git'
            }
        }
        
        stage('Build the application'){
            steps{
                bat 'mvn clean install'
            }
        }
        
        stage('Unit Test Execution'){
            steps{
                bat 'mvn test'
            }
        }
        
        stage('Build the docker image'){
            steps{
                powershell "docker build -t mathisd49/pipeline-triangle ."
            }
        }
        
        stage('Push the docker image'){
            steps{
                withCredentials([string(credentialsId:'7cc82c73-9cde-4ab3-8062-f825947808ab',variable:'dockerHubPass')]){
                    powershell "docker login -u mathisd49 -p $dockerHubPass"
                }
                
                powershell "docker push mathisd49/pipeline-triangle"
            }
        }
    }
}