# Tello_EDU_Square_mission
With sending command by Packetsender, four Tello EDU drones are connected to the same router to complete the square image circling task of four drones.

1. Download and install Packetsender
2. After tello is powered on, hold down the power button on the side of the machine for five seconds and wait for Tello EDU to restart automatically to restore factory Settings
3. Search tello's wifi signal (TELLO -- XXX-XXX) on the computer, and connect the computer to Tello through wifi
4. Send command to Tello in Packetsender. If the computer connects to Tello successfully, "OK" will be displayed at the bottom of the page.
5. Send "Battery? "Confirm drone battery level
6. Send the ROUTER SSID: XXXX and Password: XXXX required for team flight to the UAV. If the sending is successful, the wifi of TELLO -- XXX-XXX will not be displayed in the computer network interface
7. Do the same for all aircraft
8. Go to the router management page, view all devices in the current network environment, and find the MAC addresses of all tello devices that have been connected to the router.
9. Check that the environment configuration is complete before takeoff./tello/ multi-tello-formation -master/ readme.md
10. After installing the environment, open square-around-mission. py and replace tello_address with Tello's MAC address that is already connected to the router
11. Save the file and run square-around-missio.py

