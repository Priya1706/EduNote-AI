## BLE Handshake Protocol – v1

### 1. UUID Definitions
Service UUID (File Transfer):
2dd7629c-4e08-458c-bd4d-bc99f936f893

Characteristic UUID (Audio Data):
592e6f5e-6c60-4ba7-826f-067cdda070d9

### 2. Connection Steps
1. App scans for “EduNote Watch”
2. App connects to device
3. App checks for Service UUID  
4. App checks for Characteristic UUID  
5. App writes: START_TRANSFER
6. Watch sends audio chunks via notifications
7. App reassembles chunks  
8. Watch sends: END_TRANSFER
