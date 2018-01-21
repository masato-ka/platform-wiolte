"""
    Build script for test.py
    test-builder.py
"""

from os.path import join,isdir,basename
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
upload_protocol = env.subst("$UPLOAD_PROTOCOL")
FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoWio_LTE")
FRAMEWORK_VERSION = platform.get_package_version("framework-arduinoWio_LTE")
assert isdir(FRAMEWORK_DIR)

#TODO 
#warning: Ignoring missing SConscript '/Users/kawamuramasato/.platformio/packages/framework-arduinoWio_LTE/tools/platformio-build.py'
#File "/Users/kawamuramasato/.platformio/platforms/WioLTE/builder/frameworks/arduino.py", line 33, in <module>

env.Replace(
    AR="arm-none-eabi-ar",
    AS="arm-none-eabi-as",
    CC="arm-none-eabi-gcc",
    CXX="arm-none-eabi-g++",
    GDB="arm-none-eabi-gdb",
    OBJCOPY="arm-none-eabi-objcopy",
    RANLIB="arm-none-eabi-ranlib",
    SIZETOOL="arm-none-eabi-size",
    PROGNAME="firmware",
    PROGSUFFIX=".elf",
    FRAMEWORK_DIR = platform.get_package_dir("framework-arduinoWio_LTE"),
    ARFLAGS=["rcs"],
    ASFLAGS=["-x", "assembler-with-cpp"],

    CFLAGS=[
        "-c",
        "-g",
        "-Os",
        "-w",
        "-MMD",
        "-ffunction-sections",
        "-fdata-sections",
        "-nostdlib",
        "-mcpu=%s" % env.BoardConfig().get("build.cpu"),
    ],

    CCFLAGS=[
        "-c",
        "-g",
        "-Os",
        "-w",
        "-MMD",
        "-ffunction-sections",
        "-fdata-sections",
        "-nostdlib",
        "-fno-rtti",
        "-fno-exceptions",
        "-mcpu=%s" % board.get("build.mcu"),
        "-mthumb",
    ],

    CDEFINE=[
        # Define to gcc build parameter(-D Options)
        "-DSTM32_HIGH_DENSITY"
        "-DBOARD_%s" % board.get("build.variant"),
        "-D%s" % board.get("build.vect"),
        "-DERROR_LED_PORT=%s" % board.get("build.error_led_port"),
        "-DERROR_LED_PIN=%s" % board.get("build.error_led_pin"),
        "-DF_CPU=%s" % board.get("build.f_cpu"),
        "-DARDUINO=1.6",
        "-DARDUINO_WioGpsM4",
        "-DARDUINO_ARCH_ARM",
        "-D__STM32F4__",
        "-DMCU_STM32F406VG",
        "-DSTM32F2",
        "-DSTM32F4",
        "-DBOARD_discovery_f4",
        "-DARDUINO_STM32F4_WIO_GPS"
    ],

    CPPDEFINES=[
        # Define to g++ build parameter(-D Options)
        "-DSTM32_HIGH_DENSITY"
        "-DBOARD_%s" % board.get("build.variant"),
        "-D%s" % board.get("build.vect"),
        "-DERROR_LED_PORT=%s" % board.get("build.error_led_port"),
        "-DERROR_LED_PIN=%s" % board.get("build.error_led_pin"),
        "-DF_CPU=%s" % board.get("build.f_cpu"),
        "-DARDUINO=1.6",
        "-DARDUINO_WioGpsM4",
        "-DARDUINO_ARCH_ARM",
        "-D__STM32F4__",
        "-DMCU_STM32F406VG",
        "-DSTM32F2",
        "-DSTM32F4",
        "-DBOARD_discovery_f4",
        "-DARDUINO_STM32F4_WIO_GPS"
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "cores", "arduino"),
        join(FRAMEWORK_DIR, "cores", "arduino","libmaple"),
        join(FRAMEWORK_DIR, "cores", "arduino","libmaple","usbF4"),
        join(FRAMEWORK_DIR, "cores", "arduino","libmaple","usbF4","STM32_USB_Device_Library","Core","inc"),
        join(FRAMEWORK_DIR, "cores", "arduino","libmaple","usbF4","STM32_USB_Device_Library","Class", "cdc","inc"),
        join(FRAMEWORK_DIR, "cores", "arduino","libmaple","usbF4","STM32_USB_OTG_Driver","inc"),
        join(FRAMEWORK_DIR, "cores", "arduino","libmaple","usbF4","VCP"),
        join(FRAMEWORK_DIR, "cores", "arduino","avr"),
        join(FRAMEWORK_DIR, "variants", "discovery_f407"),
        join(FRAMEWORK_DIR, "libraries","WS2812"),
        join(FRAMEWORK_DIR, "libraries","Wire"),
        join(FRAMEWORK_DIR, "libraries","SPI"),
        join(FRAMEWORK_DIR, "libraries","RTClock")
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, "variants",
             env.BoardConfig().get("build.variant"), "ld")
    ],

    LINKFLAGS=[
        "-Os",
        "-Wl,--gc-sections", 
        "-mcpu=%s" % board.get("build.mcu"),
        "-Wl,-Map,$BUILD_DIR/firmware.map",
        "-lm",
        "-lgcc",
        "-mthumb",
        "-Wl,--cref",
        "-Wl,--check-sections", 
        "-Wl,--gc-sections",
        "-Wl,--unresolved-symbols=report-all",
        "-Wl,--warn-common",
        "-Wl,--warn-section-align",
        "-Wl,--warn-unresolved-symbols",
    ],

    UPLOADER="st-flash",
    UPLOADERFLAGS=[
        "write",        # write in flash
        "$SOURCES",     # firmware path to flash
        "0x08000000"    # flash start address
    ],
    UPLOADCMD='$UPLOADER $UPLOADERFLAGS',

    SIZEPRINTCMD='$SIZETOOL -B -d $SOURCES',

)

env.Append(
    ASFLAGS=env.get("CCFLAGS", [])[:],
    
    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "core", "arduino"),
        join(FRAMEWORK_DIR, "libraries")
    ],

    BUILDERS=dict(
        ElfToBin=Builder(
            action=env.VerboseAction(" ".join([
                "$OBJCOPY",
                "-O",
                "binary",
                "$SOURCES",
                "$TARGET"
            ]), "Building $TARGET"),
            suffix=".bin"
        )
    )
)

libs=[]
libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkArduino"),
    join(FRAMEWORK_DIR, "cores", "arduino")
))

libs.append(env.BuildLibrary(
        join("$BUILD_DIR", "FrameworkArduinoVariant"),
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"))
))

env.Prepend(LIBS=libs)


# Configure uploader
_upload_tool = "serial_upload"
_upload_flags = ["{upload.altID}", "{upload.usbID}"]
if upload_protocol == "dfu":
    _upload_tool = env.BoardConfig().get("upload.tool")#"maple_upload"
    _usbids = env.BoardConfig().get("upload.usbID")
    _altid = env.BoardConfig().get("upload.altID")
    _dfuse_addr = env.BoardConfig().get("upload.dfuse_addr")
    _upload_flags = [
        _altid, _usbids
    ]
    print _upload_flags
    # TODO Change suffix for OS adapt platform.
    _tool_dir = join(env.PioPlatform().get_package_dir(
    "tool-stm32tool"),"macosx")
    print "elf build and upload."
    # TODO Please fix me for UPLOAD file. $SOURCES to .pioenvs/wio_lte/firmware.elf
    env.Replace(
        UPLOAD_PORT="dfu",
        UPLOADER=join(_tool_dir,_upload_tool),
        UPLOADERFLAGS=_upload_flags,
        DFUSE_ADDR=_dfuse_addr,
#        UPLOADERFLAGS=["$UPLOAD_PORT"] + _upload_flags,
        UPLOADCMD="$UPLOADER $UPLOADERFLAGS $PROJECT_DIR/$SOURCES $DFUSE_ADDR")
else:
    print "Failed upload"
    exit(1)

#Build and Linkable firmware
target_elf = None
if "nobuild" in COMMAND_LINE_TARGETS:
    target_firm = join("$BUILD_DIR", "firmware.bin")
else:
    target_elf = env.BuildProgram()
    target_firm = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)
AlwaysBuild(env.Alias("nobuild", target_firm))
target_buildprog = env.Alias("buildprog", target_firm, target_firm)


#Size of binaru
target_size = env.Alias(
    "size", target_elf,
    env.VerboseAction("$SIZEPRINTCMD", "Calculating size $SOURCE"))
AlwaysBuild(target_size)

#
# Target: Upload by default .bin file
#

upload_actions = [env.VerboseAction("$UPLOADCMD", "Uploading $SOURCE")]

if any([
        upload_protocol.startswith("blackmagic"),
        "mbed" in env.subst("$PIOFRAMEWORK") and not upload_protocol
]):
    upload_actions.insert(0,
                          env.VerboseAction(env.AutodetectUploadPort,
                                            "Looking for upload disk..."))

elif "arduino" in env.subst("$PIOFRAMEWORK") and upload_protocol != "stlink":

    def BeforeUpload(target, source, env):
        env.AutodetectUploadPort()
        env.Replace(UPLOAD_PORT=basename(env.subst("$UPLOAD_PORT")))

    upload_actions.insert(0,
                          env.VerboseAction(BeforeUpload,
                                            "Looking for upload port..."))

AlwaysBuild(env.Alias("upload", target_firm, upload_actions))
#
# Default targets
#
Default([target_buildprog, target_size])
