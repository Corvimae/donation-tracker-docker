# GDQ Donation Tracker in k8s


#### Update static assets in S3

Exec into the pod:

```bash
kubectl exec --stdin --tty [pod-id] -- /bin/bash
```

and run:

```bash
$ python manage.py collectstatic
```