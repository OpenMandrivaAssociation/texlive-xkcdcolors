Name:		texlive-xkcdcolors
Version:	67895
Release:	1
Summary:	xkcd names of colors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xkcdcolors
License:	lppl1.3c cc0
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkcdcolors.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xkcdcolors.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In the year 2010, Randall Munroe on posted a really funny and
nice article on xkcd. He made a very curious experiment:
showing colors to a lot of people and asking to name each one.
Afterward, he processed the data and sorted the names for each
color by popularity -- that means, how many people gave the
same name to the same color. This package makes the collected
color names usable with LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xkcdcolors
%doc %{_texmfdistdir}/doc/latex/xkcdcolors

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
