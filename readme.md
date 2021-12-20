# Running Locally

## Creating a Local Cluster

### installing kind

#### Linux

```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
mv ./kind /some-dir-in-your-PATH/kind
```

#### MacOS
```
brew install kind
```

### installing kubectl

#### Linux

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

#### MacOS
```
brew install kubectl
```

### Creating a local kind cluster

```
kind create cluster --name <cluster-name>
```

### Verify Cluster status through kubectl

```
kubectl get all
```

Make sure no error is shown

### Deploying to k8s

Build and push image accordingly

change image name and tag in ```k8s/deploy.yaml``` file

```
kubectl apply -f k8s
```

### Monitor Cluster Status

```
watch kubectl get all
```


