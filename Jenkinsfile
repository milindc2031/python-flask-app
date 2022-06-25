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
		sh '##python3 test_app.py'
	}
	}

   stage('Dockerize the app') {
	 			steps{
	  docker.withRegistry('https://hub.docker.com', 'docker-creds') {

        def customImage = docker.build("haudharimilind07/python-flsk-app:${env.BUILD_ID}")
        /* Push the container to the custom Registry */
        customImage.push()
    }
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
