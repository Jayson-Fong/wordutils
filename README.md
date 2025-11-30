<!--suppress HtmlDeprecatedAttribute-->
<div align="center">
    <h1>✂️ wordutils</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [⚙️ Installation](#installation)

</div>

<hr />

# Purpose

wordutils is a simple Python package providing a suite of commands to manipulate text-based files, including
standard input. It is particularly built for wordlist creation in support of capture-the-flag exercises; however,
incorporates a broader suite of use cases, such as data normalization.

<details>
<summary>Capture-the-Flag: Wordlist Development</summary>

Capture-the-Flag (CTF) exercises frequently incorporate password security auditing or recovery using tools such as
[John the Ripper](https://www.openwall.com/john/). In certain cases, there may exist a known heuristic that can
significantly reduce the amount of time the password recovery process takes.

For example, PostgreSQL formerly leveraged MD5 hashes following this formula: `MD5(password || username)`. While the
password is unknown and is generally derived from a wordlist, the username is a known value. Hence, we can leverage
wordutils to develop a customized wordlist where our username is a suffix:

```shell
cat wordlist.txt | wordutils-suffix postgres > wordlist-postgres.txt
```

Here, a series of known, vulnerable passwords are stored in `wordlist.txt`. For each entry, we then append the word
`postgres`, the PostgreSQL default user with superuser privileges. This then saves our results into 
`wordlist-postgres.txt`, a file containing all known insecure passwords from `wordlist.txt` suffixed with `postgres`.
A tool such as [John the Ripper](https://www.openwall.com/john/) can then be used with our wordlist to recover the
password from an MD5 hash.

This example was inspired by a challenge as part of the 
[U.S. Department of Energy's 2025 CyberForce Competition](https://cyberforce.energy.gov/).

</details>

<details>
<summary>HTML Data Normalization</summary>

Given a list of entries, you can convert data to be HTML escaped and wrapped using wordutils. For example, if you have a 
list of data in a file named `promotions.txt`, you can both escape the characters and wrap the lines using wordutils.

Our proposed `promotions.txt`:

```text
50% off words
>75% off all files
```

We can then escape and wrap:

```shell
wordutils-html-escape -r promotions.txt | wordutils-wrap '<li>' '</li>'
```

Producing the following:

```text
<li>50% off words</li>
<li>&gt;75% off all files</li>
```

</details>

# Installation

<!--
`wordutils` is available on PyPI:

```shell
pip install wordutils
```
-->

You may install from source for the latest development version:

```shell
pip install git+https://github.com/Jayson-Fong/wordutils.git
```