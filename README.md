# h2o-ec2

This directory contains scripts to launch an H2O cluster in EC2.

[ STEP 0:  Install python and boto, if necessary. ]

http://boto.readthedocs.org/en/latest/

STEP 1:  Build a cluster of EC2 instances
-----------------------------------------

- Edit h2o-cluster-launch-instances.py to suit your specific environment.
- Particularly, you can update the instance type and number of worker nodes:
```
numInstancesToLaunch = 6
instanceType = 'm3.large'
```
- After changing the previous run the following:
```
./h2o-cluster-launch-instances.py
```

STEP 2:  Start H2O Cluster
-------------------------------------------------
- This will distribute the `h2o.jar` file to all the worker nodes, along with your AWS credentials and then start the H2O cluster.
```
./h2o-cluster-download-h2o.sh
./h2o-cluster-distribute-aws-credentials.sh
./h2o-cluster-start-h2o.sh
```

STEP 3:  Point your browser to H2O
----------------------------------

Point your web browser to 
    http://any one of the public DNS node addresses:54321


Stopping and restarting H2O
---------------------------
 - ./h2o-cluster-stop-h2o.sh
 - ./h2o-cluster-start-h2o.sh


Control files (generated when starting the cluster and/or H2O)
--------------------------------------------------------------

    nodes-public
        A list of H2O nodes by public DNS name.

    nodes-private
        A list of H2O nodes by private AWS IP address.

    flatfile.txt
        A list of H2O nodes by (private) IP address and port.

    latest (produced by h2o-cluster-download-h2o.sh)
        Latest build number for the requested branch.

    project_version (produced by h2o-cluster-download-h2o.sh)
        Full project version number for the requested build.

    core-site.xml (produced by ./h2o-cluster-distribute-aws-credentials.sh)
    aws_credentials.properties (produced by ./h2o-cluster-distribute-aws-credentials.sh)
        AWS credentials copied to each instance.


Stopping/Terminating the cluster
--------------------------------

Go to your Amazon AWS console and do the operation manually.
