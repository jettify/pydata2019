# Trust not, verify. How to verify algorithms with model checker

Building correct concurrent and distributed systems is a hard and very
challenging task also high complexity of such software increases the
probability of human error in design and architecture. On practice,
standard verification techniques in the industry like tests or code
reviews  are necessary but not sufficient.

In my talk we will discuss formal specification and verification language
that helps engineers design, specify, reason about and verify complex,
real-life algorithms and software systems. We will use TLA+ model checking
tool to find nasty dreadlocks, in simple python multithreading code. I also
share my experience using model checking for verification of open source
locking library for asyncio


## Usage

Copy contents of repository to the separate folder, edit `slides.tex` then
compile it with `xlatex` using command:

```bash
$ make lint
$ make pdf
```

## Source code highlighting

Slides use `minted` package for source code highlighting, it depends on
`pygments`, TLA+ requires one more package.

```bash
$ mkvirtualenv slides
$ pip install pygments
$ pip install https://github.com/hwayne/tla-pygments/archive/master.zip
```
