# Cartografo


CLI tool to generate Kubernetes ConfigMaps or Secrets with a lot of data entries from files.

One of the coolest feature in Kubernetes is to create volumes which will be used by the containers from ConfigMap or Secret objects. Otherwise, write by hand these kubernetes files is tedious, especially when we have a lot of source files:

*Example of ConfigMap with four files:*

```yaml
---
apiVersion: v1
data:
  a.txt: "kljasl\xF1djkalkas\xF1lknasdfl\xF1kasdflkajsdf\n\nalkjasfasdfads654\u1E31\
    la9ai.\xF1lkjaa\xF1ljkadf\n\xF1lkaj\xF1lkasdf.\n\n\n\xF1lkansd\xF1lknasdpfoiuqi90jql\xF1\
    kna\xF1lfkvna\xF1ldkasdf."
  b.json: "{\n    \"feature\": \"Speed\",\n    \"value\":    56,\n    \"languages\"\
    : [\n        \"sp\",\n        \"it\",\n        \"fr\",\n        \"pt\"\n    ]\n\
    }"
  c.tsv: 'ID  NAME    SCORE

    1   Pepe    56

    2   Ana     98

    3   Juan    14

    4   Julia   87'
  d: /opt/application/configuration
kind: ConfigMap
metadata:
  name: my-configmap
```

## Dependencies

**Cartografo** has been developed using Python 3.6.7 and tested using Python 3.7, 3.6 and 3.5

```bash
$ pip install -r requirements.txt
```

## How to use it

The folder path of the files is the only mandatory argument. Then there are other two optional arguments:
* K8S object: ConfigMap or Secret (Default: ConfigMap).
* Target YAML file (Default: new.yaml on working directory). If the files exists, it will be modified.

```bash
$ ./cartografo.py <files folder> --k8s-object <K8S object> --target <path to the YAML file>
```

> Remeber to have *Python3* installed and execution permission on file *cartografo.py*.


### Help

```
$ ./cartografo.py --help
```

### Create a new ConfigMap

```
$ ./cartografo.py /folder_files --k8s-object ConfigMap
```

or

```
$ ./cartografo.py /folder_files 
```

### Modify a ConfigMap

```
$ ./cartografo.py /folder_files --k8s-object ConfigMap --target /k8s/myconfigmap.yaml
```

or

```
$ ./cartografo.py /folder_files --target /k8s/myconfigmap.yaml
```




### Create a new Secret

```
$ ./cartografo.py /folder_files --k8s-object Secret
```


### Modify a Secret

```
$ ./cartografo.py /folder_files --k8s-object Secret --target /k8s/myconfigmap.yaml
```