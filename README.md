# Instalation Prerequisites
In order to use this repository you're going to need to install `g++11` and `gcc11`. The way you do this on mac is first by installing homebrew. The way to do that is https://brew.sh:
```
arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Once you've followed those instructions, then do this:
```
arch -x86_64 brew install gcc@11
```

Then give the new c compilers a test:
```
/usr/local/Cellar/gcc/11.3.0/gcc11 --version
/usr/local/Cellar/gcc/11.3.0/g++11 --version
```

If those run correctly, try the makefile in this repository.


# Stephens999 intro
Repository for the SCAT code from [Wasser et al](http://www.pnas.org/content/104/10/4228.full)

If you download this code, please take a moment to "star" the repo (click star).
This will let me know that someone is interested in using the code, which will allow me
to prioritize development. If no-one stars it I'll assume no-one finds it useful :).

Major revisions were released July 29, 2021.

- C++ software by M Stephens.  Current maintenance by Mary Kuhner (mkkuhner@uw.edu).

- Current version is version 3.0.2 (SCAT3)

- C++ code is in src/ 

- Revised manual is docs/manual.pdf; a list of changes is in this document.

##Compile
```
cd src/
make
```

##Run on example data
```
 cd src/
 ./SCAT3 ../docs/test.genotype.txt ../docs/test.location.txt . 2
```

