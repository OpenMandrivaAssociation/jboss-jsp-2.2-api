%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jsp-2.2-api
Version:          1.0.1
Release:          10.3
Summary:          JavaServer(TM) Pages 2.2 API
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              https://www.jboss.org/

# git clone git://github.com/jboss/jboss-jsp-api_spec.git jboss-jsp-2.2-api
# cd jboss-jsp-2.2-api/ && git archive --format=tar --prefix=jboss-jsp-2.2-api-1.0.1.Final/ jboss-jsp-api_2.2_spec-1.0.1.Final | xz > jboss-jsp-2.2-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    java-devel
BuildRequires:    jboss-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-servlet-3.0-api

Requires:         jpackage-utils
Requires:         jboss-el-2.2-api
Requires:         jboss-servlet-3.0-api
Requires:         java

BuildArch:        noarch

%description
JSR-000245: JavaServer(TM) Pages 2.2

%package javadoc
Summary:          Javadocs for %{name}

Requires:         jpackage-utils

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
%mvn_build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jsp-api_2.2_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.servlet.jsp:jsp-api"

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files -f .mfiles
%doc LICENSE README

%files javadoc
%doc LICENSE README
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Anthony Sasadeusz <sasadeu1@umbc.edu> 1.0.1-3
- Corrected license to CDDL or GPLv2 with exceptions.

* Mon Mar 19 2012 Anthony Sasadeusz <sasadeu1@umbc.edu> 1.0.1-2
- Added summary, changed license to GPLv2 with exceptions, expanded description,
- and added LICENSE and README files to javadoc.

* Mon Mar 19 2012 Anthony Sasadeusz <sasadeu1@umbc.edu> 1.0.1-1
- Cleanup and updated to version 1.0.1

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

