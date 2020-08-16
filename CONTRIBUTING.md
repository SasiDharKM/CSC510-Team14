# Contributing to our Project

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing to our project and its packages. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table Of Contents

1. How Can I Contribute?

    * Reporting Bugs 
    * Before Submitting A Bug Report
    * Your First Code Contribution 
    * Pull Requests 

2. Styleguides

    * Git Commit Messages 
    
  ### How Can I Contribute?
#### Reporting Bugs

This section guides you through submitting a bug report for the repository. Following these guidelines helps maintainers and the community understand your report 📝, reproduce the behavior 💻 💻, and find related reports 🔎.

Before creating bug reports, please check this list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible. Fill out the required template, the information it asks for helps us resolve issues faster.

    Note: If you find a Closed issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting A Bug Report

    Most importantly, check if you can reproduce the problem in the latest version of the package.
    Perform a cursory search to see if the problem has already been reported. If it has and the issue is still open, add a comment to the existing issue instead of opening a new one.

How Do I Submit A (Good) Bug Report?

Bugs are tracked as GitHub issues. create an issue on the repository and provide the following information by filling in the template.

Explain the problem and include additional details to help maintainers reproduce the problem:

    Use a clear and descriptive title for the issue to identify the problem.
    Describe the exact steps which reproduce the problem in as many details as possible. For example, start by explaining how you started the package, e.g. which command exactly you used in the terminal, or how you started package otherwise. When listing steps, don't just say what you did, but explain how you did it. 
    Provide specific examples to demonstrate the steps. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use Markdown code blocks.
    Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
    Explain which behavior you expected to see instead and why.
    Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem. If you use the keyboard while following the steps, record the GIF with the Keybinding Resolver shown. You can use this tool to record GIFs on macOS and Windows, and this tool or this tool on Linux.
    If the problem is related to performance or memory, include a CPU profile capture with your report.
    If the problem wasn't triggered by a specific action, describe what you were doing before the problem happened and share more information using the guidelines below.

How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as GitHub issues. After you've determined which repository your enhancement suggestion is related to, create an issue on that repository and provide the following information:

    Use a clear and descriptive title for the issue to identify the suggestion.
    Provide a step-by-step description of the suggested enhancement in as many details as possible.
    Provide specific examples to demonstrate the steps. Include copy/pasteable snippets which you use in those examples, as Markdown code blocks.
    Describe the current behavior and explain which behavior you expected to see instead and why.
    Include screenshots and animated GIFs which help you demonstrate the steps or point out the part of Atom which the suggestion is related to. You can use this tool to record GIFs on macOS and Windows, and this tool or this tool on Linux.
    Explain why this enhancement would be useful/
    List some other text editors or applications where this enhancement exists.
    Specify the name and version of the OS you're using.

#### Your First Code Contribution

#### Pull Requests

The process described here has several goals:

    Maintain code's quality
    Fix problems that are important to users
    Engage the community in working toward the best possible code structure

Please follow these steps to have your contribution considered by the maintainers:

    Follow the styleguides
    After you submit your pull request, verify that all status checks are passing
    What if the status checks are failing?
    If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted. 

### Styleguides
#### Git Commit Messages

    Use the present tense ("Add feature" not "Added feature")
    Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
    Limit the first line to 72 characters or less
    Reference issues and pull requests liberally after the first line
    When only changing documentation, include [ci skip] in the commit title
    Consider starting the commit message with an applicable emoji:
        🎨 :art: when improving the format/structure of the code
        🐎 :racehorse: when improving performance
        🚱 :non-potable_water: when plugging memory leaks
        📝 :memo: when writing docs
        🐧 :penguin: when fixing something on Linux
        🍎 :apple: when fixing something on macOS
        🏁 :checkered_flag: when fixing something on Windows
        🐛 :bug: when fixing a bug
        🔥 :fire: when removing code or files
        💚 :green_heart: when fixing the CI build
        ✅ :white_check_mark: when adding tests
        🔒 :lock: when dealing with security
        ⬆️ :arrow_up: when upgrading dependencies
        ⬇️ :arrow_down: when downgrading dependencies
        👕 :shirt: when removing linter warnings
