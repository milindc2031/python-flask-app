pipeline {
agent any
stages {
	stage('Git clone') {
		    steps {
        		 sh 'echo "Clonning the repo"'
		         }
	}
  
	stage('Test') {
	steps {
		sh 'python3 test_app.py'
		input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
	}
	}
  
  
  stage('Build Docker image') {
	steps {
    sh 'docker build -t python-fask-app:${BUILD_NUMBER} . '
	}
	}
  
  stage('Push Docker image') {
	steps {
    sh 'docker push -t python-fask-app:${BUILD_NUMBER} . '
	}
	}

  
  
	stage('Deploy')
	{
	steps {
		echo "Deploying the python-flask application"
	}
	}
}

post {
		always {
			echo 'The pipeline completed'
			junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
		}
		success {				
			echo "Flask Application Up and running!!"
		}
		failure {
			echo 'Build stage failed'
			error('Stopping early…')
		}
	}
}
