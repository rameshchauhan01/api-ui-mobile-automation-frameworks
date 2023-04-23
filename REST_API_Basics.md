Representational state transfer (REST) is a software architectural style that defines a stateless protocol.

REST is primarily used over HTTP and it makes use of HTTP GET, POST, PUT, DELETE and PATCH methods for different CRUD operations.
What is an idempotent REST API? <br/>
  If you send multiple identical requests, only the initial request would cause a change. 
  Therefore, the results returned to the user will not depend on how many times the method has been called. <br/>
## Idempotent Tables: <br/>
  |Method | Idempotent|
  |-|-|
  |HEAD   |Yes        |
  |OPTIONS|Yes        |
  |GET    |Yes        |
  |POST   |NO         |
  |PUT    |Yes        |
  |PATCH  |No         |
  |TRACE  |Yes        |
  |DELETE |Yes        |
POST:
  POST is not an idempotent method since calling it multiple times may result in incorrect updates. Usually, POST APIs create new resources on the server.
  If POST/payment endpoint is called with an identical request body, you will create multiple records. 
  To avoid this, you must have your own custom logic preventing duplicate records.   
PATCH:
  Patch is not an idempotent method because if you perform a consecutive series request with the same payload the first one will cause operation to happen 
  and the consecutive ones will cause errors.Unlike PUT which updates the entire record, PATCH can be used to update only certain fields in a record.


http://localhost:9999/restfulservices/v1/users/{id}
  http>protocol
  localhost> host or domain name
  9999> port
  restfulsefices>application content
  v1>version
  users> resource
  {id}> parameter <br/>

## Rest Vs SOAP:
    1. Rest is not standard while soap is standard
    2. Rest is light and faster compare to Soap
    3. Rest Supports only http protocol while SOAP supports other protocol like JMS,SMTP etc.
    4. XSD is used in Soap & Rest both
    5. Rest uses protocol level security (SSL) only while SOAP support both protocol level security and message level security(SOAP-WS).
    6. Soap supports WS Atomic transaction while rest is not
    7. SOAP is message orientated & Rest is resource orientated
    8. SOAP supports encoding while Rest is not.
    9. REST can generate difference types of response like XML/JSON/JPEG etc. while SOAP response is only in XML Soap format.
    10.Rest can be accessed from browser java script code while Soap is not...
    11. Rest is based on JAX-RS while SOAP is based JAX-WS
