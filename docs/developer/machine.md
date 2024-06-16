# Securing Development Machines

## Software and OS Maintenance

* Ensure that all software, including operating systems and applications (with a focus on web browsers), are kept up to date. Enabling automatic updates is advisable.
* Install applications from official app stores/package managers whenever possible. Official repositories vet applications for security before distribution.
  * macOS: Consider Homebrew for a secure and curated selection of open-source software options beyond the official App Store.
  * Windows: Consider Scoop.sh for a user-friendly alternative to manual installations that leverages trusted package repositories
* Avoid installing applications manually whenever possible.

## Firewalls and Antivirus Software

* Activate the operating system's firewall and use reputable antivirus/antimalware software, keeping them updated to protect against new threats.

## Safe Browsing and Phishing Awareness

* Be trained to recognize phishing attempts and employ safe browsing practices. Utilizing different browsers or browser profiles for different activities (personal/social versus development) is recommended.
* Be selective with browser extensions. Browser extensions can introduce vulnerabilities if not carefully vetted. Verify the source and limit the number of extensions installed. Only install extensions from reputable developers and remove any unused extensions to minimize the attack surface.

## Physical Security and Network Protection

* Physical access to development machines must be secured: these should never be left unattended and unlocked. Furthermore, machines ought to be powered off before being left unattended.
* Cover unused USB/Ethernet ports and avoid using public USB sockets, charging cables not sourced from reputable providers, and untrusted network connections, both wireless and wired.
* Enable full disk encryption and secure the machine’s boot process using a robust password.
* It's recommended to use a reputable VPN, especially on public Wi-Fi networks, and also on home networks if their security is uncertain.

## Data Backup

* Perform regular, incremental backups of the entire machine following the 3/2/1 backup rule: three copies of your data, two local on different devices, and one stored off-site. Backups shall be encrypted.
