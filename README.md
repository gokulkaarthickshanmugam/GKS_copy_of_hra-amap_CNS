# HRA-AMap

Files I have played around:
1. Usage.ipynb
2. Millitome.ipynb
3. Bidirectional Projections.ipynb
4. Registration Error Visualization.ipynb

   In this whole pipeline I havent messed around with BPCD in any manner.

One very obvious optimization I made is to directory paths are made generic and its usecases. In a way for everyone can just deploy and run. I have written a base setup script to reduce the manual tasks by the person setting it up and reducing the human error and improve productivity.

The generated projections are stored in:
/results/Projections/Backward/VHM_LeftKidney_projections-*
/results/Projections/Backward/VHM_RightKidney_projections-*

dir should have the pkl file (projections.pickle)

# Issues Faced :

1. FileNotFoundError: bcpd executable missing
   Fix:
      •	Verified bcpd was properly built and executable.
	   •	Ensured the correct path was set for cwd in subprocess.run().
	   •	Used os.path.abspath("bcpd") instead of relative paths.

2. Path Issues in Subprocess Calls: Using cwd="bcpd" caused issues when running the script from different directories.
   Fix: Updated cwd to an absolute path

3. Missing Dependencies: bcpd required additional setup before execution.
   Fix: Built bcpd using make and validated dependencies.

4. Additionally, I had a git submodule Issue (Maybe dump thing to note it but it was new thing that I learned repo within repo causing issues during the git push)
   Fix: I had to remove the repo dir (git rm --cached bcpd -r) (Thanks to chatgpt)
   
# Fixes Addressed :

1. I have handled errors in some scenarios whereever it could be potentially help us mitigate the solution, Like whenever we try to create an pre existing projections is one such scenario
2. (Not Implemented) Parallel Execution for Faster Processing to reduce execution time.
3.  Automate Projection File Naming process customized based on the scenario we can create switch like scenario in here
4.  I have written a base setup script which can be automated much more in a way that user have to just run the setup script to start working rather doing all the manual steps reading documentation. Would be much preffered by lazy developers like me :)
