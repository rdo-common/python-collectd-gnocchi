%global pypi_name collectd-gnocchi

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Output plugin for collectd that send metrics to Gnocchi

License:        ASL 2.0
URL:            http://github.com/jd/collectd-gnocchi
Source0:        https://pypi.io/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch


%package -n %{pypi_name}-common
Summary:        Common files for collectd gnocchi plugin

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Requires:  collectd
Requires:  python-%{pypi_name} == %{version}-%{release}

%description -n %{pypi_name}-common
This is a sub package which has common files for gnocchi collectd plugin

%package -n python2-%{pypi_name}
Summary:        Output plugin for collectd that send metrics to Gnocchi
%{?python_provide:%python_provide python2-collectd-gnocchi}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

Requires:  %{pypi_name}-common == %{version}-%{release}
Requires:  python-gnocchiclient >= 2.7.0
Requires:  python-keystoneauth1

%description -n python2-%{pypi_name}
This is an output plugin for collectd that send metrics to Gnocchi. It will
create a resource type named _collectd_ (by default) and a new resource for
each of the host monitored.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Output plugin for collectd that send metrics to Gnocchi
%{?python_provide:%python_provide python3-collectd-gnocchi}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:  %{pypi_name}-common == %{version}-%{release}
Requires:  python-gnocchiclient >= 2.7.0
Requires:  python3-keystoneauth1

%description -n python3-%{pypi_name}
This is an output plugin for collectd that send metrics to Gnocchi. It will
create a resource type named _collectd_ (by default) and a new resource for
each of the host monitored.

%endif

%description
This is an output plugin for collectd that send metrics to Gnocchi. It will
create a resource type named _collectd_ (by default) and a new resource for
each of the host monitored.


%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?with_python3}
LANG=en_US.UTF-8 %py3_build
%endif

%install
%py2_install
mkdir -p %{buildroot}/%{_sysconfdir}/collectd.d
cp collectd-gnocchi.conf %{buildroot}/%{_sysconfdir}/collectd.d/
cp collectd_gnocchi.py %{buildroot}/%{python2_sitelib}/

%if 0%{?with_python3}
LANG=en_US.UTF-8 %py3_install
mkdir -p %{buildroot}/%{_sysconfdir}/collectd.d
cp collectd-gnocchi.conf %{buildroot}/%{_sysconfdir}/collectd.d/
cp collectd_gnocchi.py %{buildroot}/%{python3_sitelib}/
%endif

%files -n %{pypi_name}-common
%doc README.rst
%license LICENSE
%config(noreplace) %attr(-, root, gnocchi) %{_sysconfdir}/collectd.d/collectd-gnocchi.conf


%files -n python2-%{pypi_name}
%{python2_sitelib}/collectd_gnocchi-*.egg-info
%{python2_sitelib}/collectd_gnocchi.py
%exclude %{python2_sitelib}/collectd_gnocchi.pyc
%exclude %{python2_sitelib}/collectd_gnocchi.pyo
%exclude %{python3_sitelib}/collectd_gnocchi-*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%{python3_sitelib}/collectd_gnocchi-*.egg-info
%{python3_sitelib}/collectd_gnocchi.py
%exclude %{python3_sitelib}/__pycache__/collectd_gnocchi*.pyc
%endif

%changelog
* Fri Feb 17 2017 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.0-1
- Initial package.
