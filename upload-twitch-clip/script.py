def wait_for_enter():
    input('Press [Enter] to continue... ')
    print()

def print_with_step(context: dict, msg: str):
    print(f"{context['step_no']}. {msg}")

def input_with_step(context: dict, msg: str) -> str:
    return input(f"{context['step_no']}. {msg}")

class Temp(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Clone the repo into dev/projects/{context['project_name']}.")
        wait_for_enter()

class GetTwitchURL(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Get the twitch URL")
        wait_for_enter()

class VisitVodcutter(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Visit https://twitch.center/vodcutter# and input the timestamps")
        wait_for_enter()

class GetURLs(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Click URLs and copy the contents to folderName/urls.txt")
        wait_for_enter()

class GetFileNames(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Click FFmpeg file and copy the contents to folderName/files.txt")
        wait_for_enter()

class CopyDownloadFile(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Copy the download.sh from this repo into folderName/download.sh")
        wait_for_enter()

class DownloadFiles(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Run ./download.sh")
        wait_for_enter()

class CreateOutput(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Once you have the files in the same folder, run ffmpeg -f concat -safe 0 -i files.txt -c FILE_NAME.ts")
        wait_for_enter()

class Backup(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Backup the output file")
        wait_for_enter()

class Upload(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Upload to Youtube (unlisted)")
        wait_for_enter()

def start_new_project():
    context = dict(step_no=1)
    steps = [
        GetTwitchURL(),
        VisitVodcutter(),
        GetURLs(),
        GetFileNames(),
        CopyDownloadFile(),
        DownloadFiles(),
        CreateOutput(),
        Backup(),
        Upload()
    ]
    print(f'There are {len(steps)} steps to start a new project. Ready? Go!\n')
    for step in steps:
        step.run(context)
        context['step_no'] += 1
    print('Done!')


if __name__ == "__main__":
    start_new_project()
