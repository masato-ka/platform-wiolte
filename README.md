# Wio LTE JP Ver: development platform for [PlatformIO](http://platformio.org)

The Wil LTE is released by Seeed. The board can set LTE SIM and connect to 4G/3G. Porcessor is 32-bit Flash MCUs based on the ARM Cortex-M processor(STM32F407). and The board have some Grove port. 

This development platform is 3rd party platform. Not official project.

# Instlation

## 1. Install Platform IO on VSCode.

Please install platform IO install to VSCode follow the instlaction [link](https://platformio.org/install/ide?install=vscode)

## 2. Download and extract archive.

Please download platform define from [this](https://dl.bintray.com/masato-ka/dl-package/platform-wiolte.tar.gz).
And extract platform-wiolte.tar.gz to PlathomeIO platform directory.

```bash
>tar xzvf platform-wiolte.tar.gz $HOME\.platformio\packages
```

The target path eample is below.

| platform | path|
|:----------|:---|
|Windows    | C:¥Users¥[your user]¥.platformio¥packages|
|OSX and linux | ~/.platform/packages|

Finally relunch VSCode.

## 3. Install Wio LTE for Arduino

Install Wio LTE Arduino library to Platform IO environment. Open PIO Home screen on VSCode. and click "libraries" on left pain. Fill in serch bar. It is "Wio LTE". And showed Wil LTE for Arduino. Install it.

![ Install Wio LTE for Arduino](https://github.com/masato-ka/platform-wiolte/blob/master/docs/images/instruction-image-01.png)



# Usage

## 1. Click New Projet on PIO HOME

Click "New Project" Button and showing Project Wizard Dialog.

![ Click New Project](https://github.com/masato-ka/platform-wiolte/blob/master/docs/images/instruction-image-02.png)


## 2. Fill in Project Wizard Dialog.

below table.

| Wizard form  | value                    |
|:-------------|:-------------------------|
|Name          | own new project name.    |
|Board         | "Wio LTE" choose from select box.|
|Framework     | Arduino|

![Project Wizard](https://github.com/masato-ka/platform-wiolte/blob/master/docs/images/instruction-image-03.png)

Finally click Finish. and strat create new project. please wait few minuts.

# Changeset

* 2019/3/21 version 1.2.6
    * Bug fix. g++ compaile option "f_cpu" adding. 

* 2019/3/21 version 1.2.5
    * Update Arduino framework to ver 1.2.5(JP Mirror 1.0)
    * Change Upload tool to Seeed STM32 DFU Upload tool. because bug fix.

* 2018/6/10 version 1.2.2
    * Update arduino framewark to ver 1.2.2.

# Contribution

When you contribut this project, Fork this repository and Could you create pull request.

# License 

* Under Apache 2.0 license.


# Author
* Twitter: @masato_ka
* e-mail: jp6uzv[at]gmail.com