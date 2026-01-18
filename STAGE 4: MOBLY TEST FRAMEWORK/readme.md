# Python SDET Roadmap: Mobly Specialization

A structured self-learning path focused on Android device automation using Google's Mobly framework.

## Stage 1: Python Foundational Infrastructure

- **Skills to Learn**:
  - In-depth Data Structures (`Dictionaries` for config parsing, `Lists` for device management)
  - Exception Handling (Handling device disconnection, RPC timeouts)
  - String Manipulation (Parsing logcat or shell output)
- **Practical Goal**:
  > Write a script that reads a mock YAML configuration file (simulating a Mobly config) and parses the device serial numbers into a list without crashing on missing keys.

## Stage 2: OOP for Test Frameworks

- **Skills to Learn**:
  - Class Inheritance (Understanding how to inherit from `base_test.BaseTestClass`)
  - Method Overriding (Customizing `setup_class`, `teardown_test`)
  - Scope & `self` (Sharing device objects between different test methods)
- **Practical Goal**:
  > Create a simple Python Class representing a "Device" with setup and teardown methods, simulating the lifecycle management used in Mobly.

## Stage 3: Mobly Architecture & "Hello World"

- **Skills to Learn**:
  - Mobly Configuration (`.yaml` or `.json` testbed setup)
  - Test Runner & Execution (Running tests via command line)
  - The `android_device` controller
- **Practical Goal**:
  > Write your first Mobly test script that connects to your local Android phone, retrieves its Serial Number and Android Version, and prints them to the logs.

## Stage 4: RPC & Snippets (System Control)

- **Skills to Learn**:
  - JSON-RPC Concepts (How Python talks to Java)
  - Compiling and installing `mobly-bundled-snippets`
  - Calling Android System APIs (Wi-Fi, Settings, Telephony) via Python
- **Practical Goal**:
  > Write a test case that controls the phone's hardware: Turn Wi-Fi ON, verify the state is "Enabled", then turn it OFF and verify it is "Disabled".

## Stage 5: Advanced Device Interaction

- **Skills to Learn**:
  - Android Debug Bridge (ADB) commands via Mobly
  - File Transfer (Pushing test data, pulling logs)
  - Network Interaction (Ping/HTTP requests from the device side)
- **Practical Goal**:
  > Create a test that forces the phone to connect to a specific Wi-Fi network and pings a public IP (e.g., 8.8.8.8) to validate internet connectivity.

## Stage 6: Log Analysis & Debugging

- **Skills to Learn**:
  - Understanding Mobly Test Results (`test_summary.yaml`)
  - Analyzing `logcat` (Android system logs) captured by Mobly
  - Filtering logs for specific crash or error patterns
- **Practical Goal**:
  > Intentionally write a failing test, run it, and locate the specific error trace and device logcat in the Mobly output directory.