# Autoscaling RabbitMQ Consumers with KEDA and Kubernetes

## Overview

This project demonstrates how to autoscale RabbitMQ consumer applications using Kubernetes-based Event-Driven Autoscaler (KEDA). KEDA allows you to dynamically scale your application based on metrics from various event sources, such as RabbitMQ queue length.

In this project, we'll set up a RabbitMQ server, deploy a RabbitMQ consumer application to Kubernetes, configure KEDA to monitor the RabbitMQ queue length, and observe autoscaling behavior based on the queue load.

## Prerequisites

-   Kubernetes cluster (e.g., KIND, Minikube, GKE, AKS, EKS)
-   RabbitMQ server (can be installed locally or in a cloud environment)
-   Docker (for building container images)
-   kubectl (Kubernetes command-line tool)
-   Helm (optional, for installing KEDA. I have installed KEDA using helm)


## Setup Instructions

 1. **Setup Kubernetes Cluster using KIND:**
 
> `kind create cluster --name keda-cluster`

 2. **Install KEDA**: 
	 Set up Kubernetes-based Event-Driven Autoscaler (KEDA) on your Kubernetes cluster. You can use Helm to install KEDA easily.

>     helm repo add kedacore https://kedacore.github.io/charts 
>     helm repo update
>     helm install keda kedacore/keda --namespace keda-cluster --create-namespace

 3. **Set up RabbitMQ Server**: 
	 Install and configure a RabbitMQ server. You can follow the instructions on the official [RabbitMQ website.](https://www.rabbitmq.com/docs/install-debian) I have used kali linux (debian based; distribution : bullseye)

	To start Rabbitmq-Server and management console. Use below commands.

	
>     #start rabbitmq-server 	
>     sudo systemctl start rabbitmq-server
>     
>     #enable rabbitmq-server
>     sudo systemctl enable rabbitmq-server
>     
>     #enabling management console
>     rabbitmq-plugins enable rabbitmq_management
 
Go to Management console [http://localhost:15672/](http://localhost:15672/) 

> 1. Login *user* : guest and *password* guest
> 2. Go queues and streams tab above
> 3. Enter name of the queue and create the queue
   
4. **Deploy RabbitMQ Producer**: Use a RabbitMQ producer application to send messages to the RabbitMQ queue. You can find an example producer script in this repository. (rabbitmq_producer.py)

> `pip3 install pika`
> `python3 rabbitmq_producer.py`

 5. **Deploy RabbitMQ Consumer**: Deploy a RabbitMQ consumer application to Kubernetes. This application will consume messages from the RabbitMQ queue.
 

>     kubectl apply -f rabbitmq-consumer-deployment.yaml -n keda-cluster

6.  **Configure KEDA ScaledObject**: Create a ScaledObject resource in Kubernetes to configure KEDA to monitor the RabbitMQ queue length and trigger autoscaling based on queue metrics.


>     kubectl apply -f rabbitmq-scaledobject.yaml -n keda-cluster
    
7.  **Test Autoscaling**: 
Send messages to the RabbitMQ queue and observe the autoscaling behavior of your RabbitMQ consumer application.

> `python3 rabbitmq_test.py`

8. **Monitor Autoscaling**:
Monitor the application pods and scaling events:

>     kubectl get pods -l app=rabbitmq-consumer -n keda-cluster 
>     kubectl describe scaledobject rabbitmq-scaledobject -n keda-cluster

 
## Files and Directory Structure

-   `rabbitmq_producer.py`: Example Python script for sending messages to the RabbitMQ queue.
-   `rabbitmq_consumer_deployment.yaml`: Kubernetes deployment YAML file for deploying the RabbitMQ consumer application.
-   `rabbitmq_scaledobject.yaml`: YAML file defining the ScaledObject resource for configuring KEDA autoscaling.
-   `Dockerfile`: Dockerfile for building the RabbitMQ consumer application container image.
-   `README.md`: Project README file providing an overview, setup instructions, and other details.

## Resources
-   [KEDA Documentation](https://keda.sh/docs/2.8/)
-   [RabbitMQ Documentation](https://www.rabbitmq.com/docs)
-   [Kubernetes Documentation](https://kubernetes.io/docs/home/)
-   [Docker Documentation](https://docs.docker.com/) 
- [Docker image](https://hub.docker.com/repository/docker/farhanhub/rabbitmq-producer/general)

## Contributors

-   [Farhan Ahmed](https://github.com/itsfarhan)

## License

This project is licensed under the **MIT License.**
