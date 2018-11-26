Let's edit the Dockerfile to what you would like your image to contain:

`vi Dockerfile`{{execute}}

|Command|Description
| ------ | ------ |
|i|insert text before cursor, until <Esc> hit|
|x|delete single character under cursor|
|dd|delete entire current line|
|:x<Return>|quit vi, writing out modified file to file named in original invocation|
|:wq<Return>|quit vi, writing out modified file to file named in original invocation|
|:q<Return>|quit (or exit) vi|
|:q!<Return>|quit vi even though latest changes have not been saved for this vi cal|


OR YOU CAN ALWAYS USE EMACS:


`emacs Dockerfile`{{execute}}
(ctrl-X-s saves, ctrl-X-c quits [prompts if needs to be saved)

NOTE: Emacs has some issues in Katacoda and sometimes when you exit from EMACS the command prompt starts to underline or some other strange behavior is observed. To fix that just reset the terminal attributes:

`reset`{{execute}}