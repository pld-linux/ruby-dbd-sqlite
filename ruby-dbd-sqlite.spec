Summary:	Ruby Database driver for Sqlite
Name:		ruby-dbd-sqlite
Version:	0.1.1
Release:	1
License:	Ruby License
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/44093/dbd-sqlite-%{version}.tar.gz
# Source0-md5:	ac72f75c3feedf5461b23d1da05f2b2a
URL:		http://rubyforge.org/projects/ruby-dbi/
BuildRequires:	ruby-modules
Requires:	ruby-sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby Database driver for Sqlite.

%prep
%setup -q -n dbd-sqlite-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/dbd/sqlite
%{ruby_rubylibdir}/dbd/SQLite.rb

%clean
rm -rf $RPM_BUILD_ROOT
