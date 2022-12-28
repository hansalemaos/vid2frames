import os
import subprocess
import regex
from list_all_files_recursively import get_folder_file_complete_path


def convert_video_to_frames(
    video: str, output_folder: str, fps: int = 1, fileprefix: str = "out", zfill=8
):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    procdown = subprocess.run(
        [
            "ffmpeg",
            "-i",
            video,
            "-vf",
            f"fps={fps}",
            f"{output_folder}{os.sep}{fileprefix}_%d.png",
        ],
        capture_output=False,
    )

    fi = get_folder_file_complete_path(folders=[output_folder])
    zfill += 4
    regexc = regex.compile(r"^(.*?_)(\d+\.png)$", flags=regex.I)
    pp = [
        (
            (g := regexc.search(x.file)),
            os.rename(
                x.path, os.path.join(x.folder, g.group(1) + g.group(2).zfill(zfill))
            ),
        )
        for x in fi
    ]
    fi = get_folder_file_complete_path(folders=[output_folder])
    return fi


