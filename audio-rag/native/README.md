# React Native project

Refer to instructions on React Native or:
```
yarn install
yarn build
```
the app is built as `android/audiorag.apk`

## Requirements:

### Follow [official requirements](https://reactnative.dev/docs/set-up-your-environment) or:

- Node 18 or newer
- JDK 17 (not newer)
- Android Studio with following components:
  - Android SDK
  - Android SDK Platform
  - Android Virtual Device
- Android SDK
  - API version: `Android 14 (UpsideDownCake)`
  - Install components:  
    - Android SDK Platform 34
    - Intel x86 Atom_64 System Image or Google APIs Intel x86 Atom System Image
- configure ANDROID_HOME
```shell
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```
- \[optional, for debugging] prepare virtual devices
