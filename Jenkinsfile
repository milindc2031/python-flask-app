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
				script{
	      docker.withRegistry('https://index.docker.io/v1/', 'docker-creds') {

        def customImage = docker.build("chaudharimilind07/python-flsk-app:${env.BUILD_ID}")
        /* Push the container to the custom Registry */
        customImage.push()
				}
    }
		}
		}


		stage('Deliver for development') {
            when {
                branch 'development'
            }
            steps {
                sh './jenkins/scripts/deliver-for-development.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
                sh './jenkins/scripts/kill.sh'
            }
        }
        stage('Deploy for production') {
            when {
                branch 'production'
            }
            steps {
                sh './jenkins/scripts/deploy-for-production.sh'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
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
