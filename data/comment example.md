To add comments to the code, you must add comments over each [TestClass] and [TestMethod] attribute and class properties if they do not have.
You can refer to the example here: 
```csharp
/// <summary>
/// This is a sample comment
/// </summary>
/// <param name="id">input id</param>
/// <returns>True if id matches</returns>
public bool FindId(int id)
{
    return Id == id;
}
```