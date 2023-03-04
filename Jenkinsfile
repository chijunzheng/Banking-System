 pipeline {
   agent any

   stages {
     stage('Checkout') {
       steps {
         git branch: 'main', url: 'https://github.com/chijunzheng/Banking-System'
       }
     }

     stage('Build') {
       steps {
         sh 'make build'
       }
     }

     stage('Test') {
       steps {
         sh 'pip3 install pytest'
         sh 'make test'
       }
     }

     stage('Dockerize') {
       steps {
         sh 'docker build -t ballerchi/banking-system:1.0 .'
	 sh 'docker tag ballerchi/banking-system:1.0 ballerchi/banking-system:latest'
       }
     }

     stage('Push') {
       steps {
           sh "docker login -u ballerchi -p ${password}"
         
         sh 'docker push ballerchi/banking-system:latest'
	
       }
     }
   }
 }

