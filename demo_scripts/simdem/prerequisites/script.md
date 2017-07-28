# Understanding Prerequisites

There aren't really any pre-requisites for this tutorial / demo, but
this is a convenient place to explain how they work.

# Syntax

The prerequisites section starts with a heading of `# Prerequisites`
(it can be any level heading.

The body of this section will contain 0 or more links to a script that
should be run ahead of the current one.

The scripts should appear in the order of required exection.

# Behavior

When a prerequisite script is identified SimDem will ask the user if
they have satisfied the requirement. If SimDem is running in test or
auto mode it is assumed that prerequisites have been satisified.

If the user indicates a prerequisite has been satisfied then execution
moves to the next prerequisite or onto the rest of the script.

If the user indicates a prereqiusite has not been satisfied then the
required script is executed.

If the prerequisite script contains a "Next Steps" section at the end
it will be ignored.

# Prerequisites

This section, demonstrates the prequisites. Here we define a
prequisite that is being [pulled from a GitHub repository](https://raw.githubusercontent.com/rgardler/simdem/master/demo_scripts/simdem/prerequisites/remote.md).

# Next Steps

  1. [Configure your scripts through variables](variables/script.md)
  2. [Write multi-part documents](multipart/script.md)
  3. [Use your documents as interactive tutorials or demos](running/script.md)
  4. [Use your documents as automated tests](test/script.md)
  5. [Build an SimDem container](building/script.md)
