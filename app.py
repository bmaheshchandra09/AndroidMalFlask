from flask import Flask,jsonify,request
import pyrebase
from androguard.core.bytecodes.apk import APK
from keras.models import load_model
firebaseConfig = {
  "apiKey": "AIzaSyCm0G2sIx18VD1DJRndbTvuyQhmnvSpxKU",
  "authDomain": "upload-e7fac.firebaseapp.com",
  "projectId": "upload-e7fac",
  "storageBucket": "upload-e7fac.appspot.com",
  "messagingSenderId": "805237482107",
  "appId": "1:805237482107:web:815b40db8548eddc3978de",
  "measurementId": "G-X4ST9W2NXS",
  "databaseURL":" "
}
app = Flask(__name__)
# @app.route("/",methods=['GET'])
# def home():
#   return jsonify({"message":"success"})


@app.route("/predict",methods=['GET'])
def upload():
  filename=str(request.args['query'])
  firebase_storage=pyrebase.initialize_app(firebaseConfig)
  storage=firebase_storage.storage()
  storage.child(filename).download("./",filename)
  perms=['android.permission.VIBRATE', 'android.permission.AsCCESS_COARSE_LOCATION', 'android.permission.INTERNET', 'android.permission.RECORD_AUDIO', 'android.permission.CAMERA', 'android.permission.MOUNT_UNMOUNT_FILESYSTEMS', 'android.permission.ACCESS_NETWORK_STATE', 'android.permission.WAKE_LOCK', 'android.permission.ACCESS_FINE_LOCATION', 'android.permission.GET_ACCOUNTS', 'android.permission.READ_CONTACTS', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.CALL_PHONE', 'android.permission.READ_PHONE_STATE', 'android.permission.DISABLE_KEYGUARD', 'android.permission..BILLING', 'android.permission.ACCESS_WIFI_STATE', 'android.permission.WIFI_STATE', 'android.permission.GET_TASKS', 'android.permission.NETWORK_STATE', 'android.permission.READ_EXTERNAL_STORAGE', 'android.permission.RECEIVE_BOOT_COMPLETED', 'android.permission.SYSTEM_ALERT_WINDOW', 'android.permission.USE_CREDENTIALS', 'android.permission.air.escapegamestudio.AntarcticDolphinEscape.permission.C2D_MESSAGE', 'android.permission.c2dm.permission.RECEIVE', 'android.permission.BLUETOOTH', 'android.permission.PROCESS_OUTGOING_CALLS', 'android.permission.CHANGE_WIFI_STATE', 'android.permission.SET_DEBUG_APP', 'android.permission.BATTERY_STATS', 'android.permission.BLUETOOTH_ADMIN', 'android.permission.READ_LOGS', 'android.permission.AUTHENTICATE_ACCOUNTS', 'android.permission.VIBRATION', 'android.permission.SEND_SMS', 'android.permission.READ_CALENDAR', 'android.permission.WRITE_CALENDAR', 'android.permission.MANAGE_ACCOUNTS', 'android.permission.WRITE_SYNC_SETTINGS', 'android.permission.READ_SYNC_SETTINGS', 'android.permission.RECEIVE_SMS', 'android.permission.CHANGE_NETWORK_STATE', 'android.permission.WRITE_CONTACTS', 'android.permission.READ_OWNER_DATA', 'android.permission.WRITE_OWNER_DATA', 'android.permission.FLASHLIGHT', 'android.permission.READ_SMS', 'android.permission.BROADCAST_STICKY', 'android.permission.WRITE_SETTINGS', 'android.permission.ACCESS_MOCK_LOCATION', 'android.permission.CLEAR_APP_CACHE', 'android.permission.ACCESS_SUPERUSER', 'android.permission.KILL_BACKGROUND_PROCESSES', 'android.permission.RESTART_PACKAGES', 'android.permission.MODIFY_AUDIO_SETTINGS', 'android.permission.RECEIVE_USER_PRESENT', 'android.permission.INTERACT_ACROSS_USERS_FULL', 'android.permission.READ_CALL_LOG', 'android.permission.SET_WALLPAPER_HINTS', 'android.permission.SET_WALLPAPER', 'android.permission.WRITE_SMS', 'android.permission.WRITE_CALL_LOG', 'android.permission.MODIFY_PHONE_STATE', 'android.permission.SEND_RESPOND_VIA_MESSAGE', 'android.permission.RECEIVE_MMS', 'android.permission.NFC', 'android.permission.MANAGE_DOCUMENTS', 'android.permission.PREVENT_POWER_KEY', 'android.permission.BILLING', 'android.permission.EXPAND_STATUS_BAR', 'android.permission.TRANSMIT_IR', 'android.permission.MOVE_PACKAGE', 'android.permission.BIND_ACCESSIBILITY_SERVICE', 'android.permission.GET_PACKAGE_SIZE', 'android.permission.CHANGE_CONFIGURATION', 'android.permission.WRITE_INTERNAL_STORAGE', 'android.permission.READ_PROFILE', 'android.permission.ACCESS_LOCATION_EXTRA_COMMANDS', 'android.permission.USE_FINGERPRINT', 'android.permission.ACTION_BOOT_COMPLETED', 'android.permission.UNINSTALL_SHORTCUT', 'android.permission.INSTALL_SHORTCUT', 'android.permission.SET_ALARM', 'android.permission.READ_SETTINGS', 'android.permission.REORDER_TASKS', 'android.permission.WRITE_MEDIA_STORAGE', 'android.permission.ACCESS_ALL_EXTERNAL_STORAGE', 'android.permission.PACKAGE_USAGE_STATS', 'android.permission.DELETE_CACHE_FILES', 'android.permission.WRITE_USER_DICTIONARY', 'android.permission.ACCESS_COARSE_UPDATES', 'android.permission.SUBSCRIBED_FEEDS_WRITE', 'android.permission.USE_SIP', 'android.permission.READ_SYNC_STATS', 'android.permission.DOWNLOAD_WITHOUT_NOTIFICATION', 'android.permission.ACCESS_WEATHERCLOCK_PROVIDER', 'android.permission.BIND_APPWIDGET', 'android.permission.UPDATE_DEVICE_STATS', 'android.permission.SYSTEM_OVERLAY_WINDOW', 'android.permission.READ_PHONE_SINTERNETWIFI_STATE', 'android.permission.BROADCAST_PACKAGE_INSTALL', 'android.permission.BROADCAST_PACKAGE_ADDED', 'android.permission.BROADCAST_PACKAGE_REPLACED', 'android.permission.BROADCAST_PACKAGE_CHANGED', 'android.permission.READ_INTERNAL_STORAGE', 'android.permission.sec.MDM_CERTIFICATE', 'android.permission.sec.ENTERPRISE_DEVICE_ADMIN', 'android.permission.sec.MDM_SECURITY', 'android.permission.ACCESS_DOWNLOAD_MANAGER', 'android.permission.ACCESS_ASSISTED_GPS', 'android.permission.ACCESS_GPS', 'android.permission.RECORD_VIDEO', 'android.permission.CHANGE_WIFI_MULTICAST_STATE', 'android.permission.WRITE_SECURE_SETTINGS', 'android.permission.PROCESS_INCOMING_CALLS', 'android.permission.sec.MDM_PHONE_RESTRICTION', 'android.permission.sec.MDM_LICENSE_INTERNAL', 'android.permission.sec.MDM_REMOTE_CONTROL', 'android.permission.RECEIVE_WAP_PUSH', 'android.permission.C2D_MESSAGE', 'android.permission.READ_USER_DICTIONARY', 'android.permission.SEND_DOWNLOAD_COMPLETED_INTENTS', 'android.permission.BODY_SENSORS', 'android.permission.SUBSCRIBED_FEEDS_READ', 'android.permission.SET_ORIENTATION', 'android.permission.UPDATE_APP_OPS_STATS', 'android.permission.WRITE_EXTERNALssssss_STORAGE', 'android.permission.SET_PREFERRED_APPLICATIONS', 'android.permission.PERSISTENT_ACTIVITY', 'android.permission.DEVICE_POWER', 'android.permission.STORAGE', 'android.permission.INTERNAL_SYSTEM_WINDOW', 'android.permission.ACCESS_ALL_DOWNLOADS', 'android.permission.ACCESS_DOWNLOAD_MANAGER_ADVANCED', 'android.permission.STATUS_BAR', 'android.permission.CHANGE_COMPONENT_ENABLED_STATE', 'android.permission.ACCESS_DRM', 'android.permission.READ_SECURE_SETTINGS', 'android.permission.INSTALL_DRM', 'android.permission.NETWORK', 'android.permission.BROADCAST_SMS', 'android.permission.BROADCAST_WAP_PUSH', 'android.permission.READ_MEDIA_STORAGE', 'android.permission.WRITE_APN_SETTINGS', 'android.permission.RAISED_THREAD_PRIORITY', 'android.permission.MMS_SEND_OUTBOX_MSG', 'android.permission.GLOBAL_SEARCH', 'android.permission.READ_MMS', 'android.permission.ACCESS_LOCATION', 'android.permission.CAPTURE_AUDIO_OUTPUT', 'android.permission.BAIDU_LOCATION_SERVICE', 'android.permission.ACCESS_PHONE_STATE', 'android.permission.WRITE', 'android.permission.READ_APP_BADGE', 'android.permission.STO', 'android.permission.ACCESS_CELL_ID', 'android.permission.ACCESS_CORSE_LOCATION', 'android.permission.CALL_PRIVILEGED', 'android.permission.READ_SOCIAL_STREAM', 'android.permission.WRITE_SOCIAL_STREAM', 'android.permission.MEDIA_CONTENT_CONTROL', 'android.permission.FORCE_STOP_PACKAGES', 'android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'android.permission.BIND_NOTIFICATION_LISTENER_SERVICE', 'android.permission.BLUETOOTH_PRIVILEGED', 'android.permissions.READ_DATABASE', 'android.permission.LOCATION', 'android.permission.INSTALL_PACKAGES', 'android.permission.CONNECTIVITY_INTERNAL', 'android.permission.DELETE_PACKAGES', 'android.permission.REAL_GET_TASKS', 'android.permission.MOUNT_FORMAT_FILESYSTEMS', 'android.permission.QUICKBOOT_POWERON', 'android.permission.READ_HISTORY_BOOKMARKS', 'android.permission.INJECT_EVENTS', 'android.permission.WRITE_FRAME_BUFFER', 'android.permission.READ_FRAME_BUFFER', 'android.permission.BIND_DEVICE_ADMIN', 'android.permission.ACCESS_MTK_MMHW', 'android.permission.ACCESS_WAKE_LOCK', 'android.permission.ROOT_RECOVERY_STATE', 'android.permission.LOCAL_MAC_ADDRESS', 'android.permission.RUN_INSTRUMENTATION', 'android.permission.USES_POLICY_FORCE_LOCK', 'android.permission.INTERACT_ACROSS_USERS', 'android.permission.WRITE_SECURE', 'android.permission.ADD_SYSTEM_SERVICE', 'android.permission.RECEIVE_BOOT_COMPLETE', 'android.permission.SET_ANIMATION_SCALE', 'android.permission.CLEAR_APP_USER_DATA', 'android.permission.READ_INSTALL_SESSIONS', 'android.permission.WRITE_PROFILE', 'android.permission.CHANGE_WIMAX_STATE', 'android.permission.SET_TIME_ZONE', 'android.permission.ACCESS_WIMAX_STATE', 'android.permission.READ_CELL_BROADCASTS', 'android.permission.ENABLE_KEYGUARD', 'android.permission.REBOOT', 'android.permission.SET_WALLPAPER_COMPONENT', 'android.permission.ACCESS_BLUETOOTH_SHARE', 'android.permission.GET_TOP_ACTIVITY_INFO', 'android.permission.BROADCAST_PACKAGE_REMOVED', 'android.permission.KILL_BACKGROUND_PROCESSE', 'android.permission.HARDWARE_TEST', 'android.permission.ACCESS_CHECKIN_PROPERTIES', 'android.permission.SET_PROCESS_FOREGROUND']
  vector = {}
  classes=['Safe','Malware']
  file=APK(filename)
  perm = file.get_permissions()
  model=load_model('BINARY.h5',compile=False) 
  for d in perms:
    if d in perm:
      vector[d]=1
    else:
      vector[d]=0
  input = [ v for v in vector.values() ]
  val = model.predict([input])
  if(val>=0.5):
    val=1
  else:
    val=0
  res = classes[val]
  d={}
  d['output'] = res  
  d['val']=val
  return jsonify(d)

if __name__ == "__main__":
    app.run(debug=True)