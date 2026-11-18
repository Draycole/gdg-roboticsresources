# Submissions

Share your training results here, and make your first pull request along the way.

Everyone adds **one folder** with their own name. Because nobody edits anyone else's files, your pull request will not clash with anyone else's.

## What you need

- A GitHub account
- [Git](https://git-scm.com/downloads) installed
- VS Code
- Your training curve as an image

## Words you will meet

| Word | Meaning |
|---|---|
| **Repository (repo)** | A project folder tracked by Git |
| **Fork** | Your own personal copy of someone else's repo on GitHub. So it's your copy of someone's repo that you can edit, change and make additions that you like. |
| **Clone** | Downloading a repo to your computer. So it becomes a local copy of the repo |
| **Branch** | A separate line of work, so your changes stay apart from `main` |
| **Commit** | A saved snapshot of your changes, with a message. It keeps that instant of the repo with everything you've chanegd. Plus you can add a commit message to it so everyone knows what changed with this commit. |
| **Push** | Sending your commits from your computer to GitHub |
| **Pull request (PR)** | A request for the owner to merge your changes into their repo |
| **Merge** | Combining your changes into the main project |

## Step by step

Replace `YOURNAME` with your folder name: lowercase, no spaces, letters, numbers and hyphens only. I suggest using your GitHub username cause it's unique for everyone, but then you can still use your name or a nickname if you fel it'll be cooler. Check the `submissions/` folder first to confirm.

### 1. Fork the repo

Open [github.com/Draycole/gdg-roboticsresources](https://github.com/Draycole/gdg-roboticsresources) and click **Fork** (top right), then **Create fork**. You now have a copy under your own account.

### 2. Clone your fork

Copy the address of **your fork** (it has your username in it), then either:

- **In VS Code:** press `Ctrl+Shift+P`, type `Git: Clone`, paste the address, choose a folder, and click **Open** when asked.
- **In a terminal:**
  ```bash
  git clone https://github.com/YOUR-USERNAME/gdg-roboticsresources.git
  cd gdg-roboticsresources
  ```

### 3. Tell Git who you are (this is only if you're doing this for the first time)

Open the VS Code terminal with `` Ctrl+` `` and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

To keep your email private, use the address GitHub gives you under Settings, Emails, "Keep my email addresses private". It looks like `12345+username@users.noreply.github.com`.

### 4. Create a branch

- **In VS Code:** click the branch name in the bottom-left corner (it says `main`), choose **Create new branch...**, and type `submission/YOURNAME`.
- **In a terminal:**
  ```bash
  git switch -c submission/YOURNAME
  ```

Always work on a branch, never directly on `main`.

### 5. Make your folder and add your files

Inside `cohorts/2026-27/submissions/`:

1. Create a folder named `YOURNAME`.
2. Copy `TEMPLATE.md` into it and rename the copy to `notes.md`.
3. Put your training curve in the same folder and name it `training-curve.png`.
4. Open `notes.md` and fill it in. If you used a different image name, change it in the line `![Training curve](training-curve.png)` to match.

Your folder should look like this:

```
submissions/
└── YOURNAME/
    ├── notes.md
    └── training-curve.png
```

### 6. Preview your note

In VS Code, open `notes.md` and press `Ctrl+Shift+V`. Your image should appear. If it shows as a broken link, the filename in the note does not match the image file exactly. Check capital letters and spaces.

Before you go on, look at your image. Make sure it shows no personal information (usernames, folder paths, email addresses), and that it is under 1 MB.

### 7. Commit

- **In VS Code:** click the Source Control icon (`Ctrl+Shift+G`), check that only your folder's files are listed, type the message `Add submission: YOURNAME`, and click **Commit**.
- **In a terminal:**
  ```bash
  git add cohorts/2026-27/submissions/YOURNAME
  git commit -m "Add submission: YOURNAME"
  ```

### 8. Push

- **In VS Code:** click **Publish Branch**. Sign in to GitHub in the browser if asked.
- **In a terminal:**
  ```bash
  git push -u origin submission/YOURNAME
  ```

### 9. Open a pull request

Go to your fork on GitHub. A yellow banner will offer **Compare & pull request**. Click it, and check at the top that:

- **base repository** is `Draycole/gdg-roboticsresources` and **base** is `main`
- **head repository** is your fork and **compare** is your branch

Use the title `Add submission: YOURNAME`, then click **Create pull request**.

### 10. Review

The maintainer will look at your pull request. You might be asked to change something, such as a smaller image or a fixed link. That is normal and part of the exercise. To update your pull request, make the change on the same branch, commit, and push again. It updates automatically.

When it is merged, your folder is part of the repo. Well done!

## If something goes wrong

| Problem | Fix |
|---|---|
| Image shows as a broken link | The name in `notes.md` must match the file exactly, including capitals. Avoid spaces |
| VS Code says "Please tell me who you are" | Do step 3 |
| The push asks for a password or fails | Sign in through the browser window that opens. Do not use your GitHub password in the terminal |
| My PR lists lots of files I didn't touch | You probably worked on `main`. Ask for help before continuing |
| I committed to `main` by mistake | Don't panic. Message the group chat and we'll fix it together |
| I forked before this folder existed | On your fork, click **Sync fork**, then start from step 2 |

## Can't get git working at all?

On your fork's page on GitHub, use **Add file**, then **Create new file**. Type `cohorts/2026-27/submissions/YOURNAME/notes.md` as the file name (typing the slashes creates the folders) and paste in your note. Then upload your image with **Add file**, then **Upload files**, inside that same folder. Open the pull request from there. Try the full workflow next time.