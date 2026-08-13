import random

import gifos

DIM = "\x1b[0;90m"
FG = "\x1b[0;39m"
ACCENT = "\x1b[0;92m"
BRIGHT = "\x1b[0;97m"
RESET = "\x1b[0;0m"


class ReadmeGenerator:
    def __init__(self, t: gifos.Terminal):
        self.t = t
        self.t.set_fps(18)
        self.t.set_prompt(f"{ACCENT}[thomas@nixos:~]$ {RESET}")
        self.t.toggle_blink_cursor(True)

    def boot(self, count: int = 0):
        self.t.toggle_show_cursor(False)

        out = [
            f"{DIM}[    0.924978] nixos kernel: Linux version 6.18.37 (nixbld@localhost) (gcc 15.2.0){RESET}",
            f"{DIM}[    0.925016] nixos kernel: Command line: init=/nix/store/...-nixos-system-nixos-26.11/init{RESET}",
            f"{DIM}[    0.925123] nixos kernel: NX (Execute Disable) protection: active{RESET}",
            f"{DIM}[    0.925131] nixos kernel: efi: EFI v2.7 by INSYDE Corp.{RESET}",
            f"{DIM}[    0.925169] nixos kernel: SMBIOS 3.3.0 present.{RESET}",
            f"{DIM}[    0.925174] nixos kernel: DMI: Acer Aspire A514-54/Lily_TL, BIOS V1.26 03/14/2022{RESET}",
            f"{DIM}[    0.925182] nixos kernel: tsc: Detected 2400.000 MHz processor{RESET}",
            f"{DIM}[    0.925251] nixos kernel: Secure boot disabled{RESET}",
        ]

        for row, txt in enumerate(out):
            self.t.gen_text(txt, row_num=row + 1, count=random.randint(1, count))

        self.t.clear_frame()

        out = [
            f"{ACCENT}[    0.938397] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Path Units.{RESET}",
            f"{ACCENT}[    0.938406] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Swaps.{RESET}",
            f"{ACCENT}[    0.938559] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Local File Systems.{RESET}",
            f"{ACCENT}[    0.939007] nixos systemd[1]: {BRIGHT}Started {ACCENT}Journal Service.{RESET}",
            f"{ACCENT}[    0.947075] nixos systemd[1]: {BRIGHT}Started {ACCENT}Rule-based Manager for Device Events and Files.{RESET}",
            f"{ACCENT}[    1.006905] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Basic System.{RESET}",
            f"{ACCENT}[    1.055869] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Trusted Platform Module.{RESET}",
            f"{ACCENT}[    1.685260] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Initrd Root Device.{RESET}",
            f"{ACCENT}[    1.996592] nixos systemd[1]: {BRIGHT}Mounted {ACCENT}/sysroot.{RESET}",
            f"{ACCENT}[    2.077023] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Initrd File Systems.{RESET}",
            f"{ACCENT}[    2.194194] nixos systemd[1]: {BRIGHT}Reached {ACCENT}target Switch Root.{RESET}",
        ]

        for row, txt in enumerate(out):
            self.t.gen_text(txt, row_num=row + 1, count=random.randint(1, count))

        self.t.clone_frame(15)
        self.t.clear_frame()

    def login(self):
        self.t.gen_text(f"{FG}nixos login: {RESET}", row_num=1)
        self.t.toggle_show_cursor(True)
        self.t.gen_typing_text(
            f"{BRIGHT}thomas{RESET}", row_num=1, contin=True, speed=2
        )
        self.t.toggle_show_cursor(False)

        self.t.gen_text(f"{FG}password: {RESET}", row_num=2)
        self.t.toggle_show_cursor(True)
        self.t.gen_typing_text(
            f"{BRIGHT}*******{RESET}", row_num=2, contin=True, speed=2
        )
        self.t.toggle_show_cursor(False)

        self.t.clone_frame(15)
        self.t.clear_frame()

    def about(self):
        self.t.gen_prompt(row_num=1, count=15)
        self.t.toggle_show_cursor(True)

        self.t.gen_typing_text(
            f"{BRIGHT}whoami{RESET}", row_num=1, contin=True, speed=2
        )
        self.t.toggle_show_cursor(False)

        out = [
            f"{ACCENT}User{RESET}           {FG}Thomas Cabovianco{RESET}",
            f"{ACCENT}School{RESET}         {FG}University of Buenos Aires [UBA]{RESET}",
            f"{ACCENT}Major{RESET}          {FG}Computer Engineering [In Progress]{RESET}",
            f"{ACCENT}Interests{RESET}      {FG}Programming, Linux, Machine Learning & Mobile Development{RESET}",
        ]

        self.t.gen_text(out, row_num=3)

        self.t.gen_prompt(row_num=8, count=100)
        self.t.toggle_show_cursor(True)

        self.t.clear_frame()

    def skills(self):
        self.t.gen_prompt(row_num=1, count=15)
        self.t.toggle_show_cursor(True)

        self.t.gen_typing_text(
            f"{BRIGHT}cat skills.txt{RESET}", row_num=1, contin=True, speed=2
        )
        self.t.toggle_show_cursor(False)

        out = [
            f"{ACCENT}Languages{RESET}      {FG}Kotlin, Java, Python, C, Go, Rust{RESET}",
            "\n",
            f"{ACCENT}Tools{RESET}          {FG}Git, GitHub, CI, Linux, Docker, Postman{RESET}",
            "\n",
            f"{ACCENT}Android{RESET}        {FG}Android SDK, Jetpack Compose, Material Design 3{RESET}",
            f"               {FG}MVVM, Clean Architecture{RESET}",
            f"               {FG}Kotlin Coroutines, Kotlin Flow, Navigation Compose{RESET}",
            f"               {FG}Room, Retrofit, DataStore, Kotlin Serialization, Dagger Hilt{RESET}",
            f"               {FG}Firebase Authentication, Cloud Firestore, Crashlytics{RESET}",
            f"               {FG}JUnit, MockK{RESET}",
            "\n",
            f"{ACCENT}ML{RESET}             {FG}Pandas, NumPy, PySpark{RESET}",
            f"               {FG}Matplotlib, Seaborn{RESET}",
            f"               {FG}One-Hot Encoding, Target Encoding, Standard Scaling{RESET}",
            f"               {FG}Class Imbalance Handling{RESET}",
            f"               {FG}Scikit-learn, Logistic Regression, Random Forest, XGBoost{RESET}",
            f"               {FG}Feature Engineering, Hyperparameter Tuning{RESET}",
            f"               {FG}Model Evaluation{RESET}",
        ]

        self.t.gen_text(out, row_num=3)

        self.t.gen_prompt(row_num=22, count=350)
        self.t.toggle_show_cursor(True)

        self.t.clear_frame()

    def reboot(self):
        self.t.gen_prompt(row_num=1, count=15)
        self.t.toggle_show_cursor(True)

        self.t.gen_typing_text(
            f"{BRIGHT}reboot{RESET}", row_num=1, contin=True, speed=2
        )
        self.t.toggle_show_cursor(False)

        self.t.clear_frame()

    def run(self):
        self.boot(count=5)
        self.login()
        self.about()
        self.skills()
        self.reboot()

        self.t.clear_frame()
        self.t.gen_gif()


if __name__ == "__main__":
    t = gifos.Terminal(width=900, height=520, xpad=14, ypad=14)
    g = ReadmeGenerator(t)
    g.run()
