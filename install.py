from json import dump, load

from helper import capture, centered, fill, list_extensions, parseout

with open('extensions.json', 'r+') as f:
    installed = list_extensions()
    extensions: list = load(f)
    success = 0
    for idx, e in enumerate(extensions):
        print()  # New line before header
        print(fill(f"*** Extension {str(idx).zfill(3)}: '{e}' <<", "-"))
        if e in extensions:
            success += 1
            print(">> Is already installed")
            continue
        captured = capture(['code', '--install-extension', e])
        if parseout(captured.stdout) == 'successfully':
            success += 1
            print(">> Was successfully installed")
        else:
            print(">> Failed to install")
            print(f"stdout --> {captured.stdout}")
            print(f"stderr --> {captured.stderr}")
    text = f"{success}/{len(extensions)} extensions successfully installed"
    print(centered(text)['text'])

    print("\nDumping new extensions to file...", end=" ")
    installed = list_extensions()
    f.seek(0)
    f.truncate()
    dump(installed, f, indent=2)
input("Press Enter to exit ")
