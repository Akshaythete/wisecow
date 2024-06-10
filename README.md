# Cow wisdom web server

## Prerequisites

```
sudo apt install fortune-mod cowsay -y
```

## How to use?

1. Run `./wisecow.sh`
2. Point the browser to server port (default 4499)

## What to expect?
![wisecow](https://github.com/nyrahul/wisecow/assets/9133227/8d6bfde3-4a5a-480e-8d55-3fef60300d98)

# Problem Statement
Deploy the wisecow application as a k8s app

## Requirement
1. Create Dockerfile for the image and corresponding k8s manifest to deploy in k8s env. The wisecow service should be exposed as k8s service.
2. Github action for creating new image when changes are made to this repo
3. [Challenge goal]: Enable secure TLS communication for the wisecow app.

## Expected Artifacts
1. Github repo containing the app with corresponding dockerfile, k8s manifest, any other artifacts needed.
2. Github repo with corresponding github action.
3. Github repo should be kept private and the access should be enabled for following github IDs: nyrahul, SujithKasireddy


##RESULT
![Screenshot (28)](https://github.com/Akshaythete/wisecow/assets/143180761/b2ac47b4-6367-4b3e-938a-b5fd20de7261)
![Screenshot (27)](https://github.com/Akshaythete/wisecow/assets/143180761/173237fb-1040-4b08-bd13-e734bf198b02)
![Screenshot (26)](https://github.com/Akshaythete/wisecow/assets/143180761/f32608fd-6c7f-452b-9789-276b45e098fe)




