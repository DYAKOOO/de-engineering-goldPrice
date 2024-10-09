# Table of Contents
- requirements.txt
- iac.md
- Dockerfile-consumer
- main.py
- cloud_functions.py
- pubsub_producer.py
- data_sources.py
- .gcloudignore
- pubsub_consumer.py
- Dockerfile-function
- Dockerfile-producer
- get_secret.py
- infrastructure/Pulumi.yaml
- infrastructure/os
- infrastructure/Pulumi.dev.yaml
- infrastructure/main.go
- spark_jobs/clean_transform.py
- spark_jobs/load_to_bigquery.py
- .github/workflows/version_increment.sh
- .github/workflows/main.yaml
- .github/workflows/process-gold-price.yaml

## File: requirements.txt

- Extension: .txt
- Language: plaintext
- Size: 194 bytes
- Created: 2024-10-09 12:50:36
- Modified: 2024-10-09 12:50:36

### Code

```plaintext
flask==2.0.3
werkzeug==2.0.3
google-cloud-pubsub==2.13.0
requests==2.32.2
numpy==1.23.5
pandas==1.5.3
python-dotenv==1.0.0
gunicorn==23.0.0
functions-framework==3.*
google-cloud-storage==2.13.0

```

## File: iac.md

- Extension: .md
- Language: markdown
- Size: 36146 bytes
- Created: 2024-09-25 12:17:09
- Modified: 2024-09-25 12:17:09

### Code

```markdown
# Table of Contents
- iac/Pulumi.yaml
- iac/go.mod
- iac/Pulumi.dev.yaml
- iac/go.sum
- iac/main.go

## File: iac/Pulumi.yaml

- Extension: .yaml
- Language: yaml
- Size: 149 bytes
- Created: 2024-09-23 13:47:31
- Modified: 2024-09-23 13:47:31

### Code

```yaml
name: de-goldprice
runtime: go
description: A minimal Google Cloud Go Pulumi program
config:
  pulumi:tags:
    value:
      pulumi:template: gcp-go

```

## File: iac/go.mod

- Extension: .mod
- Language: unknown
- Size: 4413 bytes
- Created: 2024-09-23 15:50:33
- Modified: 2024-09-23 15:50:33

### Code

```unknown
module de-goldprice

go 1.21

require (
	github.com/pulumi/pulumi-gcp/sdk/v7 v7.23.0
	github.com/pulumi/pulumi/sdk/v3 v3.117.0
)

require (
	dario.cat/mergo v1.0.0 // indirect
	github.com/Microsoft/go-winio v0.6.1 // indirect
	github.com/ProtonMail/go-crypto v1.0.0 // indirect
	github.com/aead/chacha20 v0.0.0-20180709150244-8b13a72661da // indirect
	github.com/agext/levenshtein v1.2.3 // indirect
	github.com/apparentlymart/go-textseg/v13 v13.0.0 // indirect
	github.com/atotto/clipboard v0.1.4 // indirect
	github.com/aymanbagabas/go-osc52/v2 v2.0.1 // indirect
	github.com/blang/semver v3.5.1+incompatible // indirect
	github.com/charmbracelet/bubbles v0.16.1 // indirect
	github.com/charmbracelet/bubbletea v0.24.2 // indirect
	github.com/charmbracelet/lipgloss v0.7.1 // indirect
	github.com/cheggaaa/pb v1.0.29 // indirect
	github.com/cloudflare/circl v1.3.7 // indirect
	github.com/containerd/console v1.0.4-0.20230313162750-1ae8d489ac81 // indirect
	github.com/cyphar/filepath-securejoin v0.2.4 // indirect
	github.com/djherbis/times v1.5.0 // indirect
	github.com/emirpasic/gods v1.18.1 // indirect
	github.com/go-git/gcfg v1.5.1-0.20230307220236-3a3c6141e376 // indirect
	github.com/go-git/go-billy/v5 v5.5.0 // indirect
	github.com/go-git/go-git/v5 v5.12.0 // indirect
	github.com/gogo/protobuf v1.3.2 // indirect
	github.com/golang/glog v1.2.0 // indirect
	github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/grpc-ecosystem/grpc-opentracing v0.0.0-20180507213350-8e809c8a8645 // indirect
	github.com/hashicorp/errwrap v1.1.0 // indirect
	github.com/hashicorp/go-multierror v1.1.1 // indirect
	github.com/hashicorp/hcl/v2 v2.17.0 // indirect
	github.com/inconshreveable/mousetrap v1.1.0 // indirect
	github.com/jbenet/go-context v0.0.0-20150711004518-d14ea06fba99 // indirect
	github.com/kevinburke/ssh_config v1.2.0 // indirect
	github.com/lucasb-eyer/go-colorful v1.2.0 // indirect
	github.com/mattn/go-isatty v0.0.19 // indirect
	github.com/mattn/go-localereader v0.0.1 // indirect
	github.com/mattn/go-runewidth v0.0.15 // indirect
	github.com/mitchellh/go-ps v1.0.0 // indirect
	github.com/mitchellh/go-wordwrap v1.0.1 // indirect
	github.com/muesli/ansi v0.0.0-20230316100256-276c6243b2f6 // indirect
	github.com/muesli/cancelreader v0.2.2 // indirect
	github.com/muesli/reflow v0.3.0 // indirect
	github.com/muesli/termenv v0.15.2 // indirect
	github.com/opentracing/basictracer-go v1.1.0 // indirect
	github.com/opentracing/opentracing-go v1.2.0 // indirect
	github.com/pgavlin/fx v0.1.6 // indirect
	github.com/pjbgf/sha1cd v0.3.0 // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/pkg/term v1.1.0 // indirect
	github.com/pulumi/appdash v0.0.0-20231130102222-75f619a67231 // indirect
	github.com/pulumi/esc v0.6.2 // indirect
	github.com/rivo/uniseg v0.4.4 // indirect
	github.com/rogpeppe/go-internal v1.11.0 // indirect
	github.com/sabhiram/go-gitignore v0.0.0-20210923224102-525f6e181f06 // indirect
	github.com/santhosh-tekuri/jsonschema/v5 v5.0.0 // indirect
	github.com/sergi/go-diff v1.3.2-0.20230802210424-5b0b94c5c0d3 // indirect
	github.com/skeema/knownhosts v1.2.2 // indirect
	github.com/spf13/cast v1.4.1 // indirect
	github.com/spf13/cobra v1.7.0 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
	github.com/texttheater/golang-levenshtein v1.0.1 // indirect
	github.com/tweekmonster/luser v0.0.0-20161003172636-3fa38070dbd7 // indirect
	github.com/uber/jaeger-client-go v2.30.0+incompatible // indirect
	github.com/uber/jaeger-lib v2.4.1+incompatible // indirect
	github.com/xanzy/ssh-agent v0.3.3 // indirect
	github.com/zclconf/go-cty v1.13.2 // indirect
	go.uber.org/atomic v1.9.0 // indirect
	golang.org/x/crypto v0.23.0 // indirect
	golang.org/x/exp v0.0.0-20231110203233-9a3e6036ecaa // indirect
	golang.org/x/mod v0.14.0 // indirect
	golang.org/x/net v0.25.0 // indirect
	golang.org/x/sync v0.6.0 // indirect
	golang.org/x/sys v0.20.0 // indirect
	golang.org/x/term v0.20.0 // indirect
	golang.org/x/text v0.15.0 // indirect
	golang.org/x/tools v0.15.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20240227224415-6ceb2ff114de // indirect
	google.golang.org/grpc v1.63.2 // indirect
	google.golang.org/protobuf v1.33.0 // indirect
	gopkg.in/warnings.v0 v0.1.2 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
	lukechampine.com/frand v1.4.2 // indirect
)

```

## File: iac/Pulumi.dev.yaml

- Extension: .yaml
- Language: yaml
- Size: 105 bytes
- Created: 2024-09-23 15:52:57
- Modified: 2024-09-23 15:52:57

### Code

```yaml
config:
  de-goldprice:project: de-goldprice
  de-goldprice:region: us-west1
  gcp:project: de-goldprice

```

## File: iac/go.sum

- Extension: .sum
- Language: unknown
- Size: 29277 bytes
- Created: 2024-09-23 15:50:33
- Modified: 2024-09-23 15:50:33

### Code

```unknown
dario.cat/mergo v1.0.0 h1:AGCNq9Evsj31mOgNPcLyXc+4PNABt905YmuqPYYpBWk=
dario.cat/mergo v1.0.0/go.mod h1:uNxQE+84aUszobStD9th8a29P2fMDhsBdgRYvZOxGmk=
github.com/HdrHistogram/hdrhistogram-go v1.1.2 h1:5IcZpTvzydCQeHzK4Ef/D5rrSqwxob0t8PQPMybUNFM=
github.com/HdrHistogram/hdrhistogram-go v1.1.2/go.mod h1:yDgFjdqOqDEKOvasDdhWNXYg9BVp4O+o5f6V/ehm6Oo=
github.com/Microsoft/go-winio v0.5.2/go.mod h1:WpS1mjBmmwHBEWmogvA2mj8546UReBk4v8QkMxJ6pZY=
github.com/Microsoft/go-winio v0.6.1 h1:9/kr64B9VUZrLm5YYwbGtUJnMgqWVOdUAXu6Migciow=
github.com/Microsoft/go-winio v0.6.1/go.mod h1:LRdKpFKfdobln8UmuiYcKPot9D2v6svN5+sAH+4kjUM=
github.com/ProtonMail/go-crypto v1.0.0 h1:LRuvITjQWX+WIfr930YHG2HNfjR1uOfyf5vE0kC2U78=
github.com/ProtonMail/go-crypto v1.0.0/go.mod h1:EjAoLdwvbIOoOQr3ihjnSoLZRtE8azugULFRteWMNc0=
github.com/aead/chacha20 v0.0.0-20180709150244-8b13a72661da h1:KjTM2ks9d14ZYCvmHS9iAKVt9AyzRSqNU1qabPih5BY=
github.com/aead/chacha20 v0.0.0-20180709150244-8b13a72661da/go.mod h1:eHEWzANqSiWQsof+nXEI9bUVUyV6F53Fp89EuCh2EAA=
github.com/agext/levenshtein v1.2.3 h1:YB2fHEn0UJagG8T1rrWknE3ZQzWM06O8AMAatNn7lmo=
github.com/agext/levenshtein v1.2.3/go.mod h1:JEDfjyjHDjOF/1e4FlBE/PkbqA9OfWu2ki2W0IB5558=
github.com/anmitsu/go-shlex v0.0.0-20200514113438-38f4b401e2be h1:9AeTilPcZAjCFIImctFaOjnTIavg87rW78vTPkQqLI8=
github.com/anmitsu/go-shlex v0.0.0-20200514113438-38f4b401e2be/go.mod h1:ySMOLuWl6zY27l47sB3qLNK6tF2fkHG55UZxx8oIVo4=
github.com/apparentlymart/go-textseg/v13 v13.0.0 h1:Y+KvPE1NYz0xl601PVImeQfFyEy6iT90AvPUL1NNfNw=
github.com/apparentlymart/go-textseg/v13 v13.0.0/go.mod h1:ZK2fH7c4NqDTLtiYLvIkEghdlcqw7yxLeM89kiTRPUo=
github.com/armon/go-socks5 v0.0.0-20160902184237-e75332964ef5 h1:0CwZNZbxp69SHPdPJAN/hZIm0C4OItdklCFmMRWYpio=
github.com/armon/go-socks5 v0.0.0-20160902184237-e75332964ef5/go.mod h1:wHh0iHkYZB8zMSxRWpUBQtwG5a7fFgvEO+odwuTv2gs=
github.com/atotto/clipboard v0.1.4 h1:EH0zSVneZPSuFR11BlR9YppQTVDbh5+16AmcJi4g1z4=
github.com/atotto/clipboard v0.1.4/go.mod h1:ZY9tmq7sm5xIbd9bOK4onWV4S6X0u6GY7Vn0Yu86PYI=
github.com/aymanbagabas/go-osc52/v2 v2.0.1 h1:HwpRHbFMcZLEVr42D4p7XBqjyuxQH5SMiErDT4WkJ2k=
github.com/aymanbagabas/go-osc52/v2 v2.0.1/go.mod h1:uYgXzlJ7ZpABp8OJ+exZzJJhRNQ2ASbcXHWsFqH8hp8=
github.com/blang/semver v3.5.1+incompatible h1:cQNTCjp13qL8KC3Nbxr/y2Bqb63oX6wdnnjpJbkM4JQ=
github.com/blang/semver v3.5.1+incompatible/go.mod h1:kRBLl5iJ+tD4TcOOxsy/0fnwebNt5EWlYSAyrTnjyyk=
github.com/bwesterb/go-ristretto v1.2.3/go.mod h1:fUIoIZaG73pV5biE2Blr2xEzDoMj7NFEuV9ekS419A0=
github.com/charmbracelet/bubbles v0.16.1 h1:6uzpAAaT9ZqKssntbvZMlksWHruQLNxg49H5WdeuYSY=
github.com/charmbracelet/bubbles v0.16.1/go.mod h1:2QCp9LFlEsBQMvIYERr7Ww2H2bA7xen1idUDIzm/+Xc=
github.com/charmbracelet/bubbletea v0.24.2 h1:uaQIKx9Ai6Gdh5zpTbGiWpytMU+CfsPp06RaW2cx/SY=
github.com/charmbracelet/bubbletea v0.24.2/go.mod h1:XdrNrV4J8GiyshTtx3DNuYkR1FDaJmO3l2nejekbsgg=
github.com/charmbracelet/lipgloss v0.7.1 h1:17WMwi7N1b1rVWOjMT+rCh7sQkvDU75B2hbZpc5Kc1E=
github.com/charmbracelet/lipgloss v0.7.1/go.mod h1:yG0k3giv8Qj8edTCbbg6AlQ5e8KNWpFujkNawKNhE2c=
github.com/cheggaaa/pb v1.0.29 h1:FckUN5ngEk2LpvuG0fw1GEFx6LtyY2pWI/Z2QgCnEYo=
github.com/cheggaaa/pb v1.0.29/go.mod h1:W40334L7FMC5JKWldsTWbdGjLo0RxUKK73K+TuPxX30=
github.com/cloudflare/circl v1.3.3/go.mod h1:5XYMA4rFBvNIrhs50XuiBJ15vF2pZn4nnUKZrLbUZFA=
github.com/cloudflare/circl v1.3.7 h1:qlCDlTPz2n9fu58M0Nh1J/JzcFpfgkFHHX3O35r5vcU=
github.com/cloudflare/circl v1.3.7/go.mod h1:sRTcRWXGLrKw6yIGJ+l7amYJFfAXbZG0kBSc8r4zxgA=
github.com/containerd/console v1.0.4-0.20230313162750-1ae8d489ac81 h1:q2hJAaP1k2wIvVRd/hEHD7lacgqrCPS+k8g1MndzfWY=
github.com/containerd/console v1.0.4-0.20230313162750-1ae8d489ac81/go.mod h1:YynlIjWYF8myEu6sdkwKIvGQq+cOckRm6So2avqoYAk=
github.com/cpuguy83/go-md2man/v2 v2.0.2/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
github.com/cyphar/filepath-securejoin v0.2.4 h1:Ugdm7cg7i6ZK6x3xDF1oEu1nfkyfH53EtKeQYTC3kyg=
github.com/cyphar/filepath-securejoin v0.2.4/go.mod h1:aPGpWjXOXUn2NCNjFvBE6aRxGGx79pTxQpKOJNYHHl4=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/djherbis/times v1.5.0 h1:79myA211VwPhFTqUk8xehWrsEO+zcIZj0zT8mXPVARU=
github.com/djherbis/times v1.5.0/go.mod h1:5q7FDLvbNg1L/KaBmPcWlVR9NmoKo3+ucqUA3ijQhA0=
github.com/elazarl/goproxy v0.0.0-20230808193330-2592e75ae04a h1:mATvB/9r/3gvcejNsXKSkQ6lcIaNec2nyfOdlTBR2lU=
github.com/elazarl/goproxy v0.0.0-20230808193330-2592e75ae04a/go.mod h1:Ro8st/ElPeALwNFlcTpWmkr6IoMFfkjXAvTHpevnDsM=
github.com/emirpasic/gods v1.18.1 h1:FXtiHYKDGKCW2KzwZKx0iC0PQmdlorYgdFG9jPXJ1Bc=
github.com/emirpasic/gods v1.18.1/go.mod h1:8tpGGwCnJ5H4r6BWwaV6OrWmMoPhUl5jm/FMNAnJvWQ=
github.com/fatih/color v1.9.0/go.mod h1:eQcE1qtQxscV5RaZvpXrrb8Drkc3/DdQ+uUYCNjL+zU=
github.com/fatih/color v1.13.0 h1:8LOYc1KYPPmyKMuN8QV2DNRWNbLo6LZ0iLs8+mlH53w=
github.com/fatih/color v1.13.0/go.mod h1:kLAiJbzzSOZDVNGyDpeOxJ47H46qBXwg5ILebYFFOfk=
github.com/gliderlabs/ssh v0.3.7 h1:iV3Bqi942d9huXnzEF2Mt+CY9gLu8DNM4Obd+8bODRE=
github.com/gliderlabs/ssh v0.3.7/go.mod h1:zpHEXBstFnQYtGnB8k8kQLol82umzn/2/snG7alWVD8=
github.com/go-git/gcfg v1.5.1-0.20230307220236-3a3c6141e376 h1:+zs/tPmkDkHx3U66DAb0lQFJrpS6731Oaa12ikc+DiI=
github.com/go-git/gcfg v1.5.1-0.20230307220236-3a3c6141e376/go.mod h1:an3vInlBmSxCcxctByoQdvwPiA7DTK7jaaFDBTtu0ic=
github.com/go-git/go-billy/v5 v5.5.0 h1:yEY4yhzCDuMGSv83oGxiBotRzhwhNr8VZyphhiu+mTU=
github.com/go-git/go-billy/v5 v5.5.0/go.mod h1:hmexnoNsr2SJU1Ju67OaNz5ASJY3+sHgFRpCtpDCKow=
github.com/go-git/go-git-fixtures/v4 v4.3.2-0.20231010084843-55a94097c399 h1:eMje31YglSBqCdIqdhKBW8lokaMrL3uTkpGYlE2OOT4=
github.com/go-git/go-git-fixtures/v4 v4.3.2-0.20231010084843-55a94097c399/go.mod h1:1OCfN199q1Jm3HZlxleg+Dw/mwps2Wbk9frAWm+4FII=
github.com/go-git/go-git/v5 v5.12.0 h1:7Md+ndsjrzZxbddRDZjF14qK+NN56sy6wkqaVrjZtys=
github.com/go-git/go-git/v5 v5.12.0/go.mod h1:FTM9VKtnI2m65hNI/TenDDDnUf2Q9FHnXYjuz9i5OEY=
github.com/gogo/protobuf v1.3.1/go.mod h1:SlYgWuQ5SjCEi6WLHjHCa1yvBfUnHcTbrrZtXPKa29o=
github.com/gogo/protobuf v1.3.2 h1:Ov1cvc58UF3b5XjBnZv7+opcTcQFZebYjWzi34vdm4Q=
github.com/gogo/protobuf v1.3.2/go.mod h1:P1XiOD3dCwIKUDQYPy72D8LYyHL2YPYrpS2s69NZV8Q=
github.com/golang/glog v1.2.0 h1:uCdmnmatrKCgMBlM4rMuJZWOkPDqdbZPnrMXDY4gI68=
github.com/golang/glog v1.2.0/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da h1:oI5xCqsCo564l8iNU+DwB5epxmsaqB+rhGL0m5jtYqE=
github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/grpc-ecosystem/grpc-opentracing v0.0.0-20180507213350-8e809c8a8645 h1:MJG/KsmcqMwFAkh8mTnAwhyKoB+sTAnY4CACC110tbU=
github.com/grpc-ecosystem/grpc-opentracing v0.0.0-20180507213350-8e809c8a8645/go.mod h1:6iZfnjpejD4L/4DwD7NryNaJyCQdzwWwH2MWhCA90Kw=
github.com/hashicorp/errwrap v1.0.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/errwrap v1.1.0 h1:OxrOeh75EUXMY8TBjag2fzXGZ40LB6IKw45YeGUDY2I=
github.com/hashicorp/errwrap v1.1.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/go-multierror v1.1.1 h1:H5DkEtf6CXdFp0N0Em5UCwQpXMWke8IA0+lD48awMYo=
github.com/hashicorp/go-multierror v1.1.1/go.mod h1:iw975J/qwKPdAO1clOe2L8331t/9/fmwbPZ6JB6eMoM=
github.com/hashicorp/hcl/v2 v2.17.0 h1:z1XvSUyXd1HP10U4lrLg5e0JMVz6CPaJvAgxM0KNZVY=
github.com/hashicorp/hcl/v2 v2.17.0/go.mod h1:gJyW2PTShkJqQBKpAmPO3yxMxIuoXkOF2TpqXzrQyx4=
github.com/inconshreveable/mousetrap v1.1.0 h1:wN+x4NVGpMsO7ErUn/mUI3vEoE6Jt13X2s0bqwp9tc8=
github.com/inconshreveable/mousetrap v1.1.0/go.mod h1:vpF70FUmC8bwa3OWnCshd2FqLfsEA9PFc4w1p2J65bw=
github.com/jbenet/go-context v0.0.0-20150711004518-d14ea06fba99 h1:BQSFePA1RWJOlocH6Fxy8MmwDt+yVQYULKfN0RoTN8A=
github.com/jbenet/go-context v0.0.0-20150711004518-d14ea06fba99/go.mod h1:1lJo3i6rXxKeerYnT8Nvf0QmHCRC1n8sfWVwXF2Frvo=
github.com/kevinburke/ssh_config v1.2.0 h1:x584FjTGwHzMwvHx18PXxbBVzfnxogHaAReU4gf13a4=
github.com/kevinburke/ssh_config v1.2.0/go.mod h1:CT57kijsi8u/K/BOFA39wgDQJ9CxiF4nAY/ojJ6r6mM=
github.com/kisielk/errcheck v1.2.0/go.mod h1:/BMXB+zMLi60iA8Vv6Ksmxu/1UDYcXs4uQLJ+jE2L00=
github.com/kisielk/errcheck v1.5.0/go.mod h1:pFxgyoBC7bSaBwPgfKdkLd5X25qrDl4LWUI2bnpBCr8=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/lucasb-eyer/go-colorful v1.2.0 h1:1nnpGOrhyZZuNyfu1QjKiUICQ74+3FNCN69Aj6K7nkY=
github.com/lucasb-eyer/go-colorful v1.2.0/go.mod h1:R4dSotOR9KMtayYi1e77YzuveK+i7ruzyGqttikkLy0=
github.com/mattn/go-colorable v0.1.4/go.mod h1:U0ppj6V5qS13XJ6of8GYAs25YV2eR4EVcfRqFIhoBtE=
github.com/mattn/go-colorable v0.1.12 h1:jF+Du6AlPIjs2BiUiQlKOX0rt3SujHxPnksPKZbaA40=
github.com/mattn/go-colorable v0.1.12/go.mod h1:u5H1YNBxpqRaxsYJYSkiCWKzEfiAb1Gb520KVy5xxl4=
github.com/mattn/go-isatty v0.0.8/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.11/go.mod h1:PhnuNfih5lzO57/f3n+odYbM4JtupLOxQOAqxQCu2WE=
github.com/mattn/go-isatty v0.0.19 h1:JITubQf0MOLdlGRuRq+jtsDlekdYPia9ZFsB8h/APPA=
github.com/mattn/go-isatty v0.0.19/go.mod h1:W+V8PltTTMOvKvAeJH7IuucS94S2C6jfK/D7dTCTo3Y=
github.com/mattn/go-localereader v0.0.1 h1:ygSAOl7ZXTx4RdPYinUpg6W99U8jWvWi9Ye2JC/oIi4=
github.com/mattn/go-localereader v0.0.1/go.mod h1:8fBrzywKY7BI3czFoHkuzRoWE9C+EiG4R1k4Cjx5p88=
github.com/mattn/go-runewidth v0.0.4/go.mod h1:LwmH8dsx7+W8Uxz3IHJYH5QSwggIsqBzpuz5H//U1FU=
github.com/mattn/go-runewidth v0.0.12/go.mod h1:RAqKPSqVFrSLVXbA8x7dzmKdmGzieGRCM46jaSJTDAk=
github.com/mattn/go-runewidth v0.0.15 h1:UNAjwbU9l54TA3KzvqLGxwWjHmMgBUVhBiTjelZgg3U=
github.com/mattn/go-runewidth v0.0.15/go.mod h1:Jdepj2loyihRzMpdS35Xk/zdY8IAYHsh153qUoGf23w=
github.com/mitchellh/go-ps v1.0.0 h1:i6ampVEEF4wQFF+bkYfwYgY+F/uYJDktmvLPf7qIgjc=
github.com/mitchellh/go-ps v1.0.0/go.mod h1:J4lOc8z8yJs6vUwklHw2XEIiT4z4C40KtWVN3nvg8Pg=
github.com/mitchellh/go-wordwrap v1.0.1 h1:TLuKupo69TCn6TQSyGxwI1EblZZEsQ0vMlAFQflz0v0=
github.com/mitchellh/go-wordwrap v1.0.1/go.mod h1:R62XHJLzvMFRBbcrT7m7WgmE1eOyTSsCt+hzestvNj0=
github.com/muesli/ansi v0.0.0-20230316100256-276c6243b2f6 h1:ZK8zHtRHOkbHy6Mmr5D264iyp3TiX5OmNcI5cIARiQI=
github.com/muesli/ansi v0.0.0-20230316100256-276c6243b2f6/go.mod h1:CJlz5H+gyd6CUWT45Oy4q24RdLyn7Md9Vj2/ldJBSIo=
github.com/muesli/cancelreader v0.2.2 h1:3I4Kt4BQjOR54NavqnDogx/MIoWBFa0StPA8ELUXHmA=
github.com/muesli/cancelreader v0.2.2/go.mod h1:3XuTXfFS2VjM+HTLZY9Ak0l6eUKfijIfMUZ4EgX0QYo=
github.com/muesli/reflow v0.3.0 h1:IFsN6K9NfGtjeggFP+68I4chLZV2yIKsXJFNZ+eWh6s=
github.com/muesli/reflow v0.3.0/go.mod h1:pbwTDkVPibjO2kyvBQRBxTWEEGDGq0FlB1BIKtnHY/8=
github.com/muesli/termenv v0.15.2 h1:GohcuySI0QmI3wN8Ok9PtKGkgkFIk7y6Vpb5PvrY+Wo=
github.com/muesli/termenv v0.15.2/go.mod h1:Epx+iuz8sNs7mNKhxzH4fWXGNpZwUaJKRS1noLXviQ8=
github.com/onsi/gomega v1.27.10 h1:naR28SdDFlqrG6kScpT8VWpu1xWY5nJRCF3XaYyBjhI=
github.com/onsi/gomega v1.27.10/go.mod h1:RsS8tutOdbdgzbPtzzATp12yT7kM5I5aElG3evPbQ0M=
github.com/opentracing/basictracer-go v1.1.0 h1:Oa1fTSBvAl8pa3U+IJYqrKm0NALwH9OsgwOqDv4xJW0=
github.com/opentracing/basictracer-go v1.1.0/go.mod h1:V2HZueSJEp879yv285Aap1BS69fQMD+MNP1mRs6mBQc=
github.com/opentracing/opentracing-go v1.1.0/go.mod h1:UkNAQd3GIcIGf0SeVgPpRdFStlNbqXla1AfSYxPUl2o=
github.com/opentracing/opentracing-go v1.2.0 h1:uEJPy/1a5RIPAJ0Ov+OIO8OxWu77jEv+1B0VhjKrZUs=
github.com/opentracing/opentracing-go v1.2.0/go.mod h1:GxEUsuufX4nBwe+T+Wl9TAgYrxe9dPLANfrWvHYVTgc=
github.com/pgavlin/fx v0.1.6 h1:r9jEg69DhNoCd3Xh0+5mIbdbS3PqWrVWujkY76MFRTU=
github.com/pgavlin/fx v0.1.6/go.mod h1:KWZJ6fqBBSh8GxHYqwYCf3rYE7Gp2p0N8tJp8xv9u9M=
github.com/pjbgf/sha1cd v0.3.0 h1:4D5XXmUUBUl/xQ6IjCkEAbqXskkq/4O7LmGn0AqMDs4=
github.com/pjbgf/sha1cd v0.3.0/go.mod h1:nZ1rrWOcGJ5uZgEEVL1VUM9iRQiZvWdbZjkKyFzPPsI=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/term v1.1.0 h1:xIAAdCMh3QIAy+5FrE8Ad8XoDhEU4ufwbaSozViP9kk=
github.com/pkg/term v1.1.0/go.mod h1:E25nymQcrSllhX42Ok8MRm1+hyBdHY0dCeiKZ9jpNGw=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/pulumi/appdash v0.0.0-20231130102222-75f619a67231 h1:vkHw5I/plNdTr435cARxCW6q9gc0S/Yxz7Mkd38pOb0=
github.com/pulumi/appdash v0.0.0-20231130102222-75f619a67231/go.mod h1:murToZ2N9hNJzewjHBgfFdXhZKjY3z5cYC1VXk+lbFE=
github.com/pulumi/esc v0.6.2 h1:+z+l8cuwIauLSwXQS0uoI3rqB+YG4SzsZYtHfNoXBvw=
github.com/pulumi/esc v0.6.2/go.mod h1:jNnYNjzsOgVTjCp0LL24NsCk8ZJxq4IoLQdCT0X7l8k=
github.com/pulumi/pulumi-gcp/sdk/v7 v7.23.0 h1:fwJvHzrxsNgxLoNkAKEm3wch9ngVG/PP1GFwfhl5n4M=
github.com/pulumi/pulumi-gcp/sdk/v7 v7.23.0/go.mod h1:CKJax8Wg7NxtKA65m5nWDIyQwaclK4ZGWJlxQkfZ8YQ=
github.com/pulumi/pulumi/sdk/v3 v3.117.0 h1:ImIsukZ2ZIYQG94uWdSZl9dJjJTosQSTsOQTauTNX7U=
github.com/pulumi/pulumi/sdk/v3 v3.117.0/go.mod h1:kNea72+FQk82OjZ3yEP4dl6nbAl2ngE8PDBc0iFAaHg=
github.com/rivo/uniseg v0.1.0/go.mod h1:J6wj4VEh+S6ZtnVlnTBMWIodfgj8LQOQFoIToxlJtxc=
github.com/rivo/uniseg v0.2.0/go.mod h1:J6wj4VEh+S6ZtnVlnTBMWIodfgj8LQOQFoIToxlJtxc=
github.com/rivo/uniseg v0.4.4 h1:8TfxU8dW6PdqD27gjM8MVNuicgxIjxpm4K7x4jp8sis=
github.com/rivo/uniseg v0.4.4/go.mod h1:FN3SvrM+Zdj16jyLfmOkMNblXMcoc8DfTHruCPUcx88=
github.com/rogpeppe/go-internal v1.11.0 h1:cWPaGQEPrBb5/AsnsZesgZZ9yb1OQ+GOISoDNXVBh4M=
github.com/rogpeppe/go-internal v1.11.0/go.mod h1:ddIwULY96R17DhadqLgMfk9H9tvdUzkipdSkR5nkCZA=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/sabhiram/go-gitignore v0.0.0-20210923224102-525f6e181f06 h1:OkMGxebDjyw0ULyrTYWeN0UNCCkmCWfjPnIA2W6oviI=
github.com/sabhiram/go-gitignore v0.0.0-20210923224102-525f6e181f06/go.mod h1:+ePHsJ1keEjQtpvf9HHw0f4ZeJ0TLRsxhunSI2hYJSs=
github.com/santhosh-tekuri/jsonschema/v5 v5.0.0 h1:TToq11gyfNlrMFZiYujSekIsPd9AmsA2Bj/iv+s4JHE=
github.com/santhosh-tekuri/jsonschema/v5 v5.0.0/go.mod h1:FKdcjfQW6rpZSnxxUvEA5H/cDPdvJ/SZJQLWWXWGrZ0=
github.com/sergi/go-diff v1.3.2-0.20230802210424-5b0b94c5c0d3 h1:n661drycOFuPLCN3Uc8sB6B/s6Z4t2xvBgU1htSHuq8=
github.com/sergi/go-diff v1.3.2-0.20230802210424-5b0b94c5c0d3/go.mod h1:A0bzQcvG0E7Rwjx0REVgAGH58e96+X0MeOfepqsbeW4=
github.com/sirupsen/logrus v1.7.0/go.mod h1:yWOB1SBYBC5VeMP7gHvWumXLIWorT60ONWic61uBYv0=
github.com/skeema/knownhosts v1.2.2 h1:Iug2P4fLmDw9f41PB6thxUkNUkJzB5i+1/exaj40L3A=
github.com/skeema/knownhosts v1.2.2/go.mod h1:xYbVRSPxqBZFrdmDyMmsOs+uX1UZC3nTN3ThzgDxUwo=
github.com/spf13/cast v1.4.1 h1:s0hze+J0196ZfEMTs80N7UlFt0BDuQ7Q+JDnHiMWKdA=
github.com/spf13/cast v1.4.1/go.mod h1:Qx5cxh0v+4UWYiBimWS+eyWzqEqokIECu5etghLkUJE=
github.com/spf13/cobra v1.7.0 h1:hyqWnYt1ZQShIddO5kBpj3vu05/++x6tJ6dg8EC572I=
github.com/spf13/cobra v1.7.0/go.mod h1:uLxZILRyS/50WlhOIKD7W6V5bgeIt+4sICxh6uRMrb0=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0 h1:4G4v2dO3VZwixGIRoQ5Lfboy6nUhCyYzaqnIAPPhYs4=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/stretchr/testify v1.5.1/go.mod h1:5W2xD1RspED5o8YsWQXVCued0rvSQ+mT+I5cxcmMvtA=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/texttheater/golang-levenshtein v1.0.1 h1:+cRNoVrfiwufQPhoMzB6N0Yf/Mqajr6t1lOv8GyGE2U=
github.com/texttheater/golang-levenshtein v1.0.1/go.mod h1:PYAKrbF5sAiq9wd+H82hs7gNaen0CplQ9uvm6+enD/8=
github.com/tweekmonster/luser v0.0.0-20161003172636-3fa38070dbd7 h1:X9dsIWPuuEJlPX//UmRKophhOKCGXc46RVIGuttks68=
github.com/tweekmonster/luser v0.0.0-20161003172636-3fa38070dbd7/go.mod h1:UxoP3EypF8JfGEjAII8jx1q8rQyDnX8qdTCs/UQBVIE=
github.com/uber/jaeger-client-go v2.30.0+incompatible h1:D6wyKGCecFaSRUpo8lCVbaOOb6ThwMmTEbhRwtKR97o=
github.com/uber/jaeger-client-go v2.30.0+incompatible/go.mod h1:WVhlPFC8FDjOFMMWRy2pZqQJSXxYSwNYOkTr/Z6d3Kk=
github.com/uber/jaeger-lib v2.4.1+incompatible h1:td4jdvLcExb4cBISKIpHuGoVXh+dVKhn2Um6rjCsSsg=
github.com/uber/jaeger-lib v2.4.1+incompatible/go.mod h1:ComeNDZlWwrWnDv8aPp0Ba6+uUTzImX/AauajbLI56U=
github.com/xanzy/ssh-agent v0.3.3 h1:+/15pJfg/RsTxqYcX6fHqOXZwwMP+2VyYWJeWM2qQFM=
github.com/xanzy/ssh-agent v0.3.3/go.mod h1:6dzNDKs0J9rVPHPhaGCukekBHKqfl+L3KghI1Bc68Uw=
github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
github.com/zclconf/go-cty v1.13.2 h1:4GvrUxe/QUDYuJKAav4EYqdM47/kZa672LwmXFmEKT0=
github.com/zclconf/go-cty v1.13.2/go.mod h1:YKQzy/7pZ7iq2jNFzy5go57xdxdWoLLpaEp4u238AE0=
go.uber.org/atomic v1.9.0 h1:ECmE8Bn/WFTYwEW/bpKD3M8VtR/zQVbavAoalC1PYyE=
go.uber.org/atomic v1.9.0/go.mod h1:fEN4uk6kAWBTFdckzkM89CLk9XfWZrxpCo0nPH17wJc=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.0.0-20220622213112-05595931fe9d/go.mod h1:IxCIyHEi3zRg3s0A5j5BB6A9Jmi73HwBIUl50j+osU4=
golang.org/x/crypto v0.3.1-0.20221117191849-2c476679df9a/go.mod h1:hebNnKkNXi2UzZN1eVRvBB7co0a+JxK6XbPiWVs/3J4=
golang.org/x/crypto v0.7.0/go.mod h1:pYwdfH91IfpZVANVyUOhSIPZaFoJGxTFbZhFTx+dXZU=
golang.org/x/crypto v0.23.0 h1:dIJU/v2J8Mdglj/8rJ6UUOM3Zc9zLZxVZwwxMooUSAI=
golang.org/x/crypto v0.23.0/go.mod h1:CKFgDieR+mRhux2Lsu27y0fO304Db0wZe70UKqHu0v8=
golang.org/x/exp v0.0.0-20231110203233-9a3e6036ecaa h1:FRnLl4eNAQl8hwxVVC17teOw8kdjVDVAiFMtgUdTSRQ=
golang.org/x/exp v0.0.0-20231110203233-9a3e6036ecaa/go.mod h1:zk2irFbV9DP96SEBUUAy67IdHUaZuSnrz1n472HUCLE=
golang.org/x/lint v0.0.0-20200302205851-738671d3881b/go.mod h1:3xt1FjdF8hUf6vQPIChWIBhFzV8gjjsPE/fR3IyQdNY=
golang.org/x/mod v0.1.1-0.20191105210325-c90efee705ee/go.mod h1:QqPTAvyqsEbceGzBzNggFXnrqF1CaUcvgkdR5Ot7KZg=
golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.8.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.14.0 h1:dGoOF9QVLYng8IHTm7BAyWqCqSheQ5pYWGhzW00YJr0=
golang.org/x/mod v0.14.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200226121028-0de0cce0169b/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200421231249-e086a090c8fd/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20201021035429-f5854403a974/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20211112202133-69e39bad7dc2/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/net v0.0.0-20220722155237-a158d28d115b/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.2.0/go.mod h1:KqCZLdyyvdV855qA2rE3GC2aiw5xGR5TEjj8smXukLY=
golang.org/x/net v0.6.0/go.mod h1:2Tu9+aMcznHK/AK1HMvgo6xiTLG5rD5rZLDS+rp2Bjs=
golang.org/x/net v0.8.0/go.mod h1:QVkue5JL9kW//ek3r6jTKnTFis1tRmNAW2P1shuFdJc=
golang.org/x/net v0.25.0 h1:d/OCCoBEUq33pjydKrGQhw7IlUPI2Oylr+8qLx49kac=
golang.org/x/net v0.25.0/go.mod h1:JkAGAh7GEvH74S6FOH42FLoXpXbE/aqXSrIQjXgsiwM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.1.0/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.6.0 h1:5BMeUDZ7vkXGfEr1x9B4bRcTH4lpkTkpdh0T/J+qjbQ=
golang.org/x/sync v0.6.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190222072716-a9d3bda3a223/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190626221950-04f50cda93cb/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191026070338-33540a1f6037/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200323222414-85ca7c5b95cd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200909081042-eff7692f9009/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200930185726-fdedc70b468f/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210124154548-22da62e12c0c/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423082822-04245dca01da/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220715151400-c0bba94af5f8/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220722155257-8c9f86f7a55f/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.1.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.2.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.3.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.5.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.6.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.20.0 h1:Od9JTbYCk261bKm4M/mw7AklTlFYIa0bIp9BgSm1S8Y=
golang.org/x/sys v0.20.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.0.0-20210927222741-03fcf44c2211/go.mod h1:jbD1KX2456YbFQfuXm/mYQcufACuNUgVhRMnK/tPxf8=
golang.org/x/term v0.2.0/go.mod h1:TVmDHMZPmdnySmBfhjOoOdhjzdE1h4u1VwSiw2l1Nuc=
golang.org/x/term v0.5.0/go.mod h1:jMB1sMXY+tzblOD4FWmEbocvup2/aLOaQEp7JmGp78k=
golang.org/x/term v0.6.0/go.mod h1:m6U89DPEgQRMq3DNkDClhWw02AUbt2daBVO4cn4Hv9U=
golang.org/x/term v0.20.0 h1:VnkxpohqXaOBYJtBmEppKUG6mXpi+4O6purfc2+sMhw=
golang.org/x/term v0.20.0/go.mod h1:8UkIAJTvZgivsXaD6/pH6U9ecQzZ45awqEOzuCvwpFY=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.6/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/text v0.4.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.7.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.8.0/go.mod h1:e1OnstbJyHTd6l/uOt8jFFHp6TRDWZR/bV3emEE/zU8=
golang.org/x/text v0.15.0 h1:h1V/4gjBv8v9cjcR6+AR5+/cIYK5N/WAgiv4xlsEtAk=
golang.org/x/text v0.15.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20181030221726-6c7e314b6563/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20200130002326-2f3ba24bd6e7/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200619180055-7c47624df98f/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/tools v0.0.0-20210106214847-113979e3529a/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.6.0/go.mod h1:Xwgl3UAJ/d3gWutnCtw505GrjyAbvKui8lOU390QaIU=
golang.org/x/tools v0.15.0 h1:zdAyfUGbYmuVokhzVmghFl2ZJh5QhcfebBgmVPFYA+8=
golang.org/x/tools v0.15.0/go.mod h1:hpksKq4dtpQWS1uQ61JkdqWM3LscIS6Slf+VVkm+wQk=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/genproto/googleapis/rpc v0.0.0-20240227224415-6ceb2ff114de h1:cZGRis4/ot9uVm639a+rHCUaG0JJHEsdyzSQTMX+suY=
google.golang.org/genproto/googleapis/rpc v0.0.0-20240227224415-6ceb2ff114de/go.mod h1:H4O17MA/PE9BsGx3w+a+W2VOLLD1Qf7oJneAoU6WktY=
google.golang.org/grpc v1.63.2 h1:MUeiw1B2maTVZthpU5xvASfTh3LDbxHd6IJ6QQVU+xM=
google.golang.org/grpc v1.63.2/go.mod h1:WAX/8DgncnokcFUldAxq7GeB5DXHDbMF+lLvDomNkRA=
google.golang.org/protobuf v1.33.0 h1:uNO2rsAINq/JlFpSdYEKIZ0uKD/R9cpdv0T+yoGwGmI=
google.golang.org/protobuf v1.33.0/go.mod h1:c6P6GXX6sHbq/GpV6MGZEdwhWPcYBgnhAHhKbcUYpos=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/warnings.v0 v0.1.2 h1:wFXVbFY8DY5/xOe1ECiWdKCzZlxgshcYVNkBHstARME=
gopkg.in/warnings.v0 v0.1.2/go.mod h1:jksf8JmL6Qr/oQM2OXTHunEvvTAsrWBLb6OOjuVWRNI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
lukechampine.com/frand v1.4.2 h1:RzFIpOvkMXuPMBb9maa4ND4wjBn71E1Jpf8BzJHMaVw=
lukechampine.com/frand v1.4.2/go.mod h1:4S/TM2ZgrKejMcKMbeLjISpJMO+/eZ1zu3vYX9dtj3s=
pgregory.net/rapid v0.5.5 h1:jkgx1TjbQPD/feRoK+S/mXw9e1uj6WilpHrXJowi6oA=
pgregory.net/rapid v0.5.5/go.mod h1:PY5XlDGj0+V1FCq0o192FdRhpKHGTRIWBgqjDBTrq04=

```

## File: iac/main.go

- Extension: .go
- Language: go
- Size: 1263 bytes
- Created: 2024-09-23 16:07:31
- Modified: 2024-09-23 16:07:31

### Code

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/container"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Load configuration
		conf := config.New(ctx, "")
		project := conf.Get("project")
		if project == "" {
			project = "de-goldprice" // Default project if not specified
		}
		region := conf.Get("region")
		if region == "" {
			region = "us-west1" // Default to us-west1 if not specified
		}

		// Create an Autopilot GKE cluster with a new name
		cluster, err := container.NewCluster(ctx, "gold-price-cluster-new", &container.ClusterArgs{
			Project:          pulumi.String(project),
			Location:         pulumi.String(region),
			EnableAutopilot:  pulumi.Bool(true),
			ReleaseChannel:   &container.ClusterReleaseChannelArgs{
				Channel: pulumi.String("REGULAR"),
			},
			VerticalPodAutoscaling: &container.ClusterVerticalPodAutoscalingArgs{
				Enabled: pulumi.Bool(true),
			},
			DeletionProtection: pulumi.Bool(false),
		})
		if err != nil {
			return err
		}

		// Export the cluster name and endpoint
		ctx.Export("clusterName", cluster.Name)
		ctx.Export("clusterEndpoint", cluster.Endpoint)

		return nil
	})
}
```


```

## File: Dockerfile-consumer

- Extension: 
- Language: unknown
- Size: 195 bytes
- Created: 2024-09-30 14:52:25
- Modified: 2024-09-30 14:52:25

### Code

```unknown
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pubsub_consumer.py .
COPY data_sources.py .

CMD ["python", "pubsub_consumer.py"]

```

## File: main.py

- Extension: .py
- Language: python
- Size: 924 bytes
- Created: 2024-10-07 14:42:09
- Modified: 2024-10-07 14:42:09

### Code

```python
from data_sources import fetch_gold_price, fetch_central_bank_data, fetch_mining_data, fetch_market_data
from pubsub_producer import publish_to_pubsub
from datetime import datetime
from cloud_functions import process_pubsub

def main():
    date_str = datetime.now().strftime('%Y%m%d')
    
    # Fetch data from various sources
    gold_price_data = fetch_gold_price(date_str)
    central_bank_data = fetch_central_bank_data(date_str)
    mining_data = fetch_mining_data(date_str)
    market_data = fetch_market_data(date_str)
    
    # Publish data to Pub/Sub
    if gold_price_data:
        publish_to_pubsub('gold-prices', gold_price_data)
    if central_bank_data:
        publish_to_pubsub('central-bank-data', central_bank_data)
    if mining_data:
        publish_to_pubsub('mining-data', mining_data)
    if market_data:
        publish_to_pubsub('market-data', market_data)

if __name__ == "__main__":
    main()

```

## File: cloud_functions.py

- Extension: .py
- Language: python
- Size: 229 bytes
- Created: 2024-10-07 14:21:44
- Modified: 2024-10-07 14:21:44

### Code

```python
import functions_framework
import logging

logging.basicConfig(level=logging.INFO)

@functions_framework.cloud_event
def process_pubsub(cloud_event):
    logging.info("Cloud Function triggered successfully!")
    return 'OK', 200
```

## File: pubsub_producer.py

- Extension: .py
- Language: python
- Size: 3287 bytes
- Created: 2024-10-09 12:49:52
- Modified: 2024-10-09 12:49:52

### Code

```python
import os
import logging
from flask import Flask, jsonify
from google.cloud import pubsub_v1
import json
from datetime import datetime
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Get environment variables
BASE_URL = os.environ.get('GOLD_API_BASE_URL', 'https://www.goldapi.io/api')
GOLD_API_KEY = os.environ.get('GOLD_API_KEY')
PROJECT_ID = os.environ.get('GOOGLE_CLOUD_PROJECT')
PUBSUB_TOPIC = os.environ.get('PUBSUB_TOPIC', 'gold-price')
GCS_BUCKET = os.environ.get('GCS_BUCKET', 'gold-price-raw-data')


def fetch_gold_price(date):
    url = f"{BASE_URL}/XAU/USD"
    headers = {'x-access-token': GOLD_API_KEY}
    
    logger.info(f"Fetching gold price from API for date: {date}")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
 
        return {
            'date': date,
            'price': data.get('price'),
            'open_price': data.get('open_price'),
            'high_price': data.get('high_price'),
            'low_price': data.get('low_price')
        }
    except requests.RequestException as e:
        logger.error(f"Error fetching gold price data: {str(e)}")
        return None

def publish_to_pubsub(data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC)
    
    data_str = json.dumps(data).encode("utf-8")
    try:
        future = publisher.publish(topic_path, data_str)
        message_id = future.result(timeout=30)
        logger.info(f"Published message ID: {message_id}")
        return True
    except Exception as e:
        logger.error(f"Error publishing to Pub/Sub: {str(e)}")
        return False


def write_to_gcs(data):
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(f'gold_price_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    blob.upload_from_string(json.dumps(data))
    logger.info(f"Data written to GCS: {blob.name}")
    
@app.route('/fetch-and-publish')
def fetch_and_publish():
    data = {...}  # The fetched data

    # Write to GCS
    client = storage.Client()
    bucket = client.bucket('gold-price-raw-data')
    blob = bucket.blob(f'gold_price_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    blob.upload_from_string(json.dumps(data))


    try:
        date_str = datetime.now().strftime('%Y-%m-%d')
        price_data = fetch_gold_price(date_str)
        if price_data:
            if publish_to_pubsub(price_data):
                return jsonify({"status": "success", "data": price_data}), 200
            else:
                return jsonify({"status": "error", "message": "Failed to publish to Pub/Sub"}), 500
        else:
            return jsonify({"status": "error", "message": "Failed to fetch gold price data"}), 500
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
    return jsonify({"status": "success", "data": data})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
```

## File: data_sources.py

- Extension: .py
- Language: python
- Size: 3239 bytes
- Created: 2024-09-30 12:54:08
- Modified: 2024-09-30 12:54:08

### Code

```python
import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv


load_dotenv()

#
API_KEY = os.getenv('GOLD_API_KEY')
FRED_API_KEY = os.getenv('FRED_API_KEY')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

#Gold Price Data
API_KEY = os.getenv('GOLD_API_KEY')
BASE_URL = 'https://www.goldapi.io/api'

def fetch_gold_price(date):
    url = f"{BASE_URL}/XAU/USD/{date}"
    headers = {'x-access-token': API_KEY}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': data.get('date', date),  # Use the input date if 'date' is not in the response
            'price': data.get('price'),
            'open': data.get('open_price'),
            'high': data.get('high_price'),
            'low': data.get('low_price')
        }
    else:
        print(f"Error fetching gold price data for {date}: {response.status_code}")
        return None
        
def fetch_central_bank_data(date):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&observation_start={date}&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': date,
            'federal_funds_rate': float(data['observations'][-1]['value'])
        }
    else:
        print(f"Error fetching central bank data for {date}: {response.status_code}")
        return None

def fetch_mining_data(date):
    # As an example, we'll use Alpha Vantage to fetch stock data for a major gold mining company
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=NEM&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': date,
            'newmont_stock_price': float(data['Global Quote']['05. price'])
        }
    else:
        print(f"Error fetching mining data for {date}: {response.status_code}")
        return None

def fetch_market_data(date):
    # We'll use Alpha Vantage again to fetch S&P 500 data as a market indicator
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': date,
            'sp500_price': float(data['Global Quote']['05. price'])
        }
    else:
        print(f"Error fetching market data for {date}: {response.status_code}")
        return None


def main():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)  # Fetch last 30 days of data
    
    data = []
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y%m%d')
        price_data = fetch_gold_price(date_str)
        if price_data:
            data.append(price_data)
        current_date += timedelta(days=1)
    
    df = pd.DataFrame(data)
    df.to_csv('gold_prices.csv', index=False)
    print(f"Data saved to gold_prices.csv")

if __name__ == "__main__":
    main()
```

## File: .gcloudignore

- Extension: 
- Language: unknown
- Size: 62 bytes
- Created: 2024-10-04 17:06:15
- Modified: 2024-10-04 17:06:15

### Code

```unknown
.git
.gitignore
node_modules
__pycache__
*.pyc
.env
venv/
*.md
```

## File: pubsub_consumer.py

- Extension: .py
- Language: python
- Size: 1293 bytes
- Created: 2024-09-30 15:17:05
- Modified: 2024-09-30 15:17:05

### Code

```python
from google.cloud import pubsub_v1
import json
from google.cloud import storage
from datetime import datetime
import os

PROJECT_ID = os.getenv('GCP_PROJECT_ID')
if not PROJECT_ID:
    raise ValueError("GCP_PROJECT_ID environment variable is not set")
SUBSCRIPTION_NAME = 'gold-prices-sub'
BUCKET_NAME = 'gold-price-raw-data'

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME)

storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

def store_in_gcs(data):
    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    blob = bucket.blob(f'gold_price_{date_str}.json')
    blob.upload_from_string(json.dumps(data))
    print(f"Stored data in GCS: gs://{BUCKET_NAME}/{blob.name}")

def callback(message):
    print(f"Received message: {message.data}")
    data = json.loads(message.data)
    store_in_gcs(data)
    message.ack()

def main():
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}")

    try:
        streaming_pull_future.result()
    except Exception as e:
        streaming_pull_future.cancel()
        print(f"Listening for messages has stopped: {e}")

if __name__ == "__main__":
    main()
```

## File: Dockerfile-function

- Extension: 
- Language: unknown
- Size: 197 bytes
- Created: 2024-10-07 14:29:26
- Modified: 2024-10-07 14:29:26

### Code

```unknown
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec functions-framework --target=process_pubsub --signature-type=http
```

## File: Dockerfile-producer

- Extension: 
- Language: unknown
- Size: 637 bytes
- Created: 2024-10-03 14:09:21
- Modified: 2024-10-03 14:09:21

### Code

```unknown
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# Run the application with Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 pubsub_producer:app
```

## File: get_secret.py

- Extension: .py
- Language: python
- Size: 763 bytes
- Created: 2024-09-19 16:54:35
- Modified: 2024-09-19 16:54:35

### Code

```python
import os
from kubernetes import client, config

def get_secret(secret_name, key):
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        # We're running in Kubernetes
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        secret = v1.read_namespaced_secret(secret_name, 'default')
        return base64.b64decode(secret.data[key]).decode('utf-8')
    else:
        # We're running locally
        from dotenv import load_dotenv
        load_dotenv()
        return os.getenv(key)

# Usage
GOLD_API_KEY = get_secret('api-secrets', 'gold-api-key')
FRED_API_KEY = get_secret('api-secrets', 'fred-api-key')
ALPHA_VANTAGE_API_KEY = get_secret('api-secrets', 'alpha-vantage-api-key')
KAFKA_PASSWORD = get_secret('kafka-secrets', 'kafka-password')
```

## File: infrastructure/Pulumi.yaml

- Extension: .yaml
- Language: yaml
- Size: 149 bytes
- Created: 2024-09-23 13:47:31
- Modified: 2024-09-23 13:47:31

### Code

```yaml
name: de-goldprice
runtime: go
description: A minimal Google Cloud Go Pulumi program
config:
  pulumi:tags:
    value:
      pulumi:template: gcp-go

```

## File: infrastructure/os

- Extension: 
- Language: unknown
- Size: 0 bytes
- Created: 2024-10-01 15:49:11
- Modified: 2024-10-01 15:49:11

### Code

```unknown

```

## File: infrastructure/Pulumi.dev.yaml

- Extension: .yaml
- Language: yaml
- Size: 59 bytes
- Created: 2024-10-04 11:25:37
- Modified: 2024-10-04 11:25:37

### Code

```yaml
config:
  gcp:project: de-goldprice
  gcp:zone: us-west1-a

```

## File: infrastructure/main.go

- Extension: .go
- Language: go
- Size: 8441 bytes
- Created: 2024-10-09 11:19:49
- Modified: 2024-10-09 11:19:49

### Code

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/bigquery"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/pubsub"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/compute"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/cloudrun"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/monitoring"
)


func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Load configuration
		conf := config.New(ctx, "")
		project := conf.Get("project")
		if project == "" {
			project = "de-goldprice"
		}
		region := conf.Get("region")
		if region == "" {
			region = "us-west1"
		}
		zone := conf.Get("zone")
		if zone == "" {
			zone = "us-west1-a"
		}

		// Import existing buckets
		rawDataBucket, err := storage.NewBucket(ctx, "gold-price-raw-data", &storage.BucketArgs{
			Name:     pulumi.String("gold-price-raw-data"),
			Location: pulumi.String("US"),
			Project:  pulumi.String(project),
		}, pulumi.Import(pulumi.ID("gold-price-raw-data")))
		if err != nil {
			return err
		}

		processedDataBucket, err := storage.NewBucket(ctx, "gold-price-processed-data", &storage.BucketArgs{
			Name:     pulumi.String("gold-price-processed-data"),
			Location: pulumi.String("US"),
			Project:  pulumi.String(project),
		}, pulumi.Import(pulumi.ID("gold-price-processed-data")))
		if err != nil {
			return err
		}

		codeBucket, err := storage.NewBucket(ctx, "de-goldprice-code", &storage.BucketArgs{
			Name:     pulumi.String("de-goldprice-code"),
			Location: pulumi.String("US"),
			Project:  pulumi.String(project),
		}, pulumi.Import(pulumi.ID("de-goldprice-code")))
		if err != nil {
			return err
		}
		// Create Pub/Sub topic
		topicName := "gold-price"
		topic, err := pubsub.NewTopic(ctx, topicName, &pubsub.TopicArgs{
			Name:    pulumi.String(topicName),
			Project: pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create Pub/Sub subscription
		_, err = pubsub.NewSubscription(ctx, "gold-price-subscription", &pubsub.SubscriptionArgs{
			Name:    pulumi.String("gold-price-sub"),
			Topic:   topic.Name,
			Project: pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create a Compute Engine instance for Spark
		sparkInstance, err := compute.NewInstance(ctx, "spark-instance", &compute.InstanceArgs{
			Name:        pulumi.String("spark-instance"),
			MachineType: pulumi.String("n1-standard-4"),
			Zone:        pulumi.String(zone),
			BootDisk: &compute.InstanceBootDiskArgs{
				InitializeParams: &compute.InstanceBootDiskInitializeParamsArgs{
					Image: pulumi.String("ubuntu-os-cloud/ubuntu-2004-lts"),
				},
			},
			NetworkInterfaces: compute.InstanceNetworkInterfaceArray{
				&compute.InstanceNetworkInterfaceArgs{
					Network: pulumi.String("default"),
					AccessConfigs: compute.InstanceNetworkInterfaceAccessConfigArray{
						&compute.InstanceNetworkInterfaceAccessConfigArgs{},
					},
				},
			},
			Metadata: pulumi.StringMap{
				"startup-script": pulumi.String(`
					#!/bin/bash
					apt-get update
					apt-get install -y openjdk-11-jdk
					wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
					tar xvf spark-3.1.2-bin-hadoop3.2.tgz
					mv spark-3.1.2-bin-hadoop3.2 /opt/spark
					echo "export PATH=$PATH:/opt/spark/bin" >> /etc/environment
				`),
			},
			Tags: pulumi.StringArray{
				pulumi.String("spark"),
			},
		})
		if err != nil {
			return err
		}

		// Create BigQuery dataset
		datasetName := "gold_price_dataset"
		dataset, err := bigquery.NewDataset(ctx, datasetName, &bigquery.DatasetArgs{
			DatasetId: pulumi.String(datasetName),
			Location:  pulumi.String("US"),
			Project:   pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create BigQuery table
		table, err := bigquery.NewTable(ctx, "gold_prices", &bigquery.TableArgs{
			DatasetId: dataset.DatasetId,
			TableId:   pulumi.String("gold_prices"),
			Project:   pulumi.String(project),
			Schema: pulumi.String(`[
				{
					"name": "date",
					"type": "DATE",
					"mode": "REQUIRED"
				},
				{
					"name": "price",
					"type": "FLOAT",
					"mode": "REQUIRED"
				},
				{
					"name": "open_price",
					"type": "FLOAT",
					"mode": "NULLABLE"
				},
				{
					"name": "high_price",
					"type": "FLOAT",
					"mode": "NULLABLE"
				},
				{
					"name": "low_price",
					"type": "FLOAT",
					"mode": "NULLABLE"
				}
			]`),
			TimePartitioning: &bigquery.TableTimePartitioningArgs{
				Type:  pulumi.String("DAY"),
				Field: pulumi.String("date"),
			},
		})
		if err != nil {
			return err
		}

		// Create a view for 30-day moving average
		_, err = bigquery.NewTable(ctx, "gold_price_30day_avg", &bigquery.TableArgs{
			DatasetId: dataset.DatasetId,
			TableId:   pulumi.String("gold_price_30day_avg"),
			Project:   pulumi.String(project),
			View: &bigquery.TableViewArgs{
				Query: pulumi.Sprintf(`
					SELECT
						date,
						price,
						AVG(price) OVER (ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS moving_avg_30day
					FROM
						%s.%s.gold_prices
					ORDER BY
						date DESC
				`, project, dataset.DatasetId),
				UseLegacySql: pulumi.Bool(false),
			},
		})
		if err != nil {
			return err
		}

		// Cloud Run service
		_, err = cloudrun.NewService(ctx, "gold-price-ingestion", &cloudrun.ServiceArgs{
			Location: pulumi.String(region),
			Project:  pulumi.String(project),
			Template: &cloudrun.ServiceTemplateArgs{
				Spec: &cloudrun.ServiceTemplateSpecArgs{
					Containers: cloudrun.ServiceTemplateSpecContainerArray{
						&cloudrun.ServiceTemplateSpecContainerArgs{
							Image: pulumi.String("gcr.io/de-goldprice/gold-price-producer:v1.0.27"),
							Envs: cloudrun.ServiceTemplateSpecContainerEnvArray{
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("PUBSUB_TOPIC"),
									Value: topic.Name,
								},
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("GOOGLE_CLOUD_PROJECT"),
									Value: pulumi.String(project),
								},
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("GOLD_API_BASE_URL"),
									Value: pulumi.String("https://www.goldapi.io/api"),
								},
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("GOLD_API_KEY"),
									Value: pulumi.String("goldapi-1192n117m18se8at-io"), // Consider using a secret manager for this
								},
							},
							Ports: cloudrun.ServiceTemplateSpecContainerPortArray{
								&cloudrun.ServiceTemplateSpecContainerPortArgs{
									ContainerPort: pulumi.Int(8080),
								},
							},
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create a Cloud Monitoring alert policy
		_, err = monitoring.NewAlertPolicy(ctx, "gold-price-alert", &monitoring.AlertPolicyArgs{
			DisplayName: pulumi.String("Gold Price Service Alert"),
			Combiner:    pulumi.String("OR"),
			Conditions: monitoring.AlertPolicyConditionArray{
				&monitoring.AlertPolicyConditionArgs{
					DisplayName: pulumi.String("High error rate"),
					ConditionThreshold: &monitoring.AlertPolicyConditionConditionThresholdArgs{
						Filter:     pulumi.String("resource.type = \"cloud_run_revision\" AND resource.labels.service_name = \"gold-price-ingestion\" AND metric.type = \"run.googleapis.com/request_count\" AND metric.labels.response_code_class = \"5xx\""),
						Duration:   pulumi.String("60s"),
						Comparison: pulumi.String("COMPARISON_GT"),
						ThresholdValue: pulumi.Float64(5),
						Aggregations: monitoring.AlertPolicyConditionConditionThresholdAggregationArray{
							&monitoring.AlertPolicyConditionConditionThresholdAggregationArgs{
								AlignmentPeriod:  pulumi.String("60s"),
								PerSeriesAligner: pulumi.String("ALIGN_RATE"),
							},
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		// Export resources
		ctx.Export("pubsubTopic", topic.Name)
		ctx.Export("sparkInstanceName", sparkInstance.Name)
		ctx.Export("sparkInstanceIP", sparkInstance.NetworkInterfaces.Index(pulumi.Int(0)).AccessConfigs().Index(pulumi.Int(0)).NatIp())
		ctx.Export("bigQueryTableId", table.ID())
		ctx.Export("rawDataBucketName", rawDataBucket.Name)
		ctx.Export("processedDataBucketName", processedDataBucket.Name)
		ctx.Export("codeBucketName", codeBucket.Name)

		return nil
	})
}
```

## File: spark_jobs/clean_transform.py

- Extension: .py
- Language: python
- Size: 1845 bytes
- Created: 2024-10-09 12:08:56
- Modified: 2024-10-09 12:08:56

### Code

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, coalesce, lit
from pyspark.sql.types import StructType, StructField, StringType, FloatType, DateType

def main():
    spark = SparkSession.builder.appName("GoldPriceCleanTransform").getOrCreate()
    
    # Set GCS configuration
    spark._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    
    schema = StructType([
        StructField("date", StringType(), True),
        StructField("price", FloatType(), True),
        StructField("open", FloatType(), True),
        StructField("high", FloatType(), True),
        StructField("low", FloatType(), True)
    ])

    input_path = "gs://gold-price-raw-data/*.json"
    output_path = "gs://gold-price-processed-data/cleaned"

    print(f"Reading data from: {input_path}")
    df = spark.read.json(input_path, schema=schema)

    print("Input data sample:")
    df.show(5)
    print(f"Input data count: {df.count()}")

    cleaned_df = df.select(
        to_date(col("date"), "yyyyMMdd").alias("date"),
        coalesce(col("price"), lit(0.0)).alias("price"),
        coalesce(col("open"), lit(0.0)).alias("open_price"),
        coalesce(col("high"), lit(0.0)).alias("high_price"),
        coalesce(col("low"), lit(0.0)).alias("low_price")
    ).filter(col("date").isNotNull())

    print("Cleaned data sample:")
    cleaned_df.show(5)
    print(f"Cleaned data count: {cleaned_df.count()}")

    print(f"Writing cleaned data to: {output_path}")
    cleaned_df.write.partitionBy("date").parquet(output_path, mode="overwrite")

    print("Data cleaning and transformation completed successfully")

if __name__ == "__main__":
    main()
```

## File: spark_jobs/load_to_bigquery.py

- Extension: .py
- Language: python
- Size: 2279 bytes
- Created: 2024-10-09 12:09:05
- Modified: 2024-10-09 12:09:05

### Code

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def main():
    
    spark = SparkSession.builder.appName("GoldPriceCleanTransform").getOrCreate()
    
    # Set GCS configuration
    spark._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    

    schema = StructType([
        StructField("date", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("open_price", DoubleType(), True),
        StructField("high_price", DoubleType(), True),
        StructField("low_price", DoubleType(), True)
    ])

    input_path = "gs://gold-price-processed-data/cleaned"
    print(f"Reading data from: {input_path}")
    df = spark.read.schema(schema).parquet(input_path)

    print("Schema of input data:")
    df.printSchema()

    print("Input data sample:")
    df.show(5, truncate=False)

    print("Data types of columns:")
    df.dtypes

    # Convert date from string to date type
    df = df.withColumn("date", to_date(col("date")))

    # Ensure price columns are of DoubleType
    for column in ["price", "open_price", "high_price", "low_price"]:
        df = df.withColumn(column, col(column).cast(DoubleType()))

    print("Schema after transformations:")
    df.printSchema()

    print("Data sample after transformations:")
    df.show(5, truncate=False)

    print(f"Input data count: {df.count()}")

    output_table = "de-goldprice.gold_price_dataset.gold_prices"
    print(f"Writing data to BigQuery table: {output_table}")
    
    df.write \
        .format("bigquery") \
        .option("table", output_table) \
        .option("temporaryGcsBucket", "gold-price-temp-bucket") \
        .mode("overwrite") \
        .save()

    print("Data loaded to BigQuery successfully")

    # Verify data in BigQuery
    bq_df = spark.read.format("bigquery").option("table", output_table).load()
    print("Data in BigQuery:")
    bq_df.show(5, truncate=False)
    print(f"BigQuery data count: {bq_df.count()}")

if __name__ == "__main__":
    main()
```

## File: .github/workflows/version_increment.sh

- Extension: .sh
- Language: bash
- Size: 630 bytes
- Created: 2024-10-09 16:47:07
- Modified: 2024-10-09 15:59:19

### Code

```bash
#!/bin/bash

# Fetch the latest version
LATEST_VERSION=$(gcloud container images list-tags gcr.io/de-goldprice/gold-price-producer --format='get(tags)' --sort-by=~tags | grep '^v1\.0\.' | head -n 1)

# Extract and increment patch version
PATCH_VERSION=$(echo $LATEST_VERSION | cut -d. -f3)
NEW_PATCH_VERSION=$((PATCH_VERSION + 1))
NEW_VERSION="v1.0.$NEW_PATCH_VERSION"

# Build and push the new version
docker build -t gcr.io/de-goldprice/gold-price-producer:$NEW_VERSION -f Dockerfile-producer .
docker push gcr.io/de-goldprice/gold-price-producer:$NEW_VERSION

# Output the new version for use in other scripts
echo $NEW_VERSION
```

## File: .github/workflows/main.yaml

- Extension: .yaml
- Language: yaml
- Size: 3636 bytes
- Created: 2024-10-09 16:45:32
- Modified: 2024-10-09 16:45:32

### Code

```yaml
name: main

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * *' # Runs at 00:00 UTC every day

env:
  PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
  REGION: us-west1

jobs:
  deploy:
    name: Deploy to GCP
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Setup Go
      uses: actions/setup-go@v2
      with:
        go-version: '1.21'

    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Authenticate to Google Cloud
      uses: google-github-actions/auth@v1
      with:
        credentials_json: ${{ secrets.GCP_SA_KEY }}

    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v1
      with:
        project_id: ${{ env.PROJECT_ID }}

    - name: Configure Docker
      run: |
        gcloud auth configure-docker gcr.io

    - name: Build and Push New Version
      id: build_version
      run: |
        NEW_VERSION=$(./version_increment.sh)
        echo "NEW_VERSION=$NEW_VERSION" >> $GITHUB_OUTPUT
        docker build -t gcr.io/${{ env.PROJECT_ID }}/gold-price-producer:$NEW_VERSION -f Dockerfile-producer .
        docker push gcr.io/${{ env.PROJECT_ID }}/gold-price-producer:$NEW_VERSION

    - name: Deploy to Cloud Run
      run: |
        gcloud run deploy gold-price-ingestion \
          --image gcr.io/${{ env.PROJECT_ID }}/gold-price-producer:${{ steps.build_version.outputs.NEW_VERSION }} \
          --region ${{ env.REGION }} \
          --set-env-vars GCS_BUCKET=gold-price-raw-data \
          --service-account goldprice-service-account@${{ env.PROJECT_ID }}.iam.gserviceaccount.com

    - name: Update Cloud Function
      run: |
        gcloud functions deploy process_gold_price \
          --gen2 \
          --runtime python310 \
          --region ${{ env.REGION }} \
          --source . \
          --entry-point process_pubsub \
          --trigger-http \
          --allow-unauthenticated

    - name: Copy Spark scripts to Compute Engine
      run: |
        gcloud compute scp spark_jobs/* spark-instance:~/ --zone us-west1-a

    - name: Run Spark Jobs
      run: |
        gcloud compute ssh spark-instance --zone us-west1-a --command "
        spark-submit \
        --master local[*] \
        clean_transform.py && \
        spark-submit \
        --master local[*] \
        load_to_bigquery.py
        "

    - name: Trigger Cloud Run Service
      run: |
        CLOUD_RUN_URL=$(gcloud run services describe gold-price-ingestion --region ${{ env.REGION }} --format='value(status.url)')
        curl -X GET ${CLOUD_RUN_URL}/fetch-and-publish

    - name: Verify Deployment
      run: |
        gcloud run services describe gold-price-ingestion --region ${{ env.REGION }}
        gcloud functions describe process_gold_price --region ${{ env.REGION }}

    - name: Verify BigQuery Data
      run: |
        bq query --use_legacy_sql=false '
        SELECT COUNT(*) as row_count
        FROM `de-goldprice.gold_price_dataset.gold_prices`
        WHERE DATE(date) = DATE(CURRENT_TIMESTAMP())
        '

    - name: Clean up old images
      run: |
        OLD_VERSIONS=$(gcloud container images list-tags gcr.io/${{ env.PROJECT_ID }}/gold-price-producer --format='get(tags)' --sort-by=~tags | tail -n +6)
        for version in $OLD_VERSIONS; do
          gcloud container images delete gcr.io/${{ env.PROJECT_ID }}/gold-price-producer:$version --quiet
        done
```

## File: .github/workflows/process-gold-price.yaml

- Extension: .yaml
- Language: yaml
- Size: 1745 bytes
- Created: 2024-10-09 16:01:24
- Modified: 2024-10-09 16:01:24

### Code

```yaml
name: Process Gold Price Data

on:
  schedule:
    - cron: '0 */12 * * *' # Runs every 12 hours
  workflow_dispatch: # Allows manual triggering

jobs:
  process-data:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install google-cloud-pubsub google-cloud-bigquery google-cloud-storage

    - name: Authenticate to Google Cloud
      uses: 'google-github-actions/auth@v1'
      with:
        credentials_json: '${{ secrets.GCP_SA_KEY }}'

    - name: Set up Cloud SDK
      uses: google-github-actions/setup-gcloud@v1

    - name: Trigger Cloud Run Service
      run: |
        CLOUD_RUN_URL=$(gcloud run services describe gold-price-ingestion --region us-west1 --format='value(status.url)')
        curl -X GET ${CLOUD_RUN_URL}/fetch-and-publish

    - name: Run Spark Jobs
      run: |
        gcloud compute ssh spark-instance --zone us-west1-a --command "
        spark-submit \
        --master local[*] \
        clean_transform.py && \
        spark-submit \
        --master local[*] \
        load_to_bigquery.py
        "

    - name: Verify BigQuery Data
      run: |
        bq query --use_legacy_sql=false '
        SELECT COUNT(*) as row_count
        FROM `de-goldprice.gold_price_dataset.gold_prices`
        WHERE DATE(date) = DATE(CURRENT_TIMESTAMP())
        '

    env:
      PROJECT_ID: de-goldprice
      PUBSUB_TOPIC: gold-price
      BIGQUERY_DATASET: gold_price_dataset
      BIGQUERY_TABLE: gold_prices
      GOOGLE_APPLICATION_CREDENTIALS: ${{ steps.auth.outputs.credentials_file_path }}
```

