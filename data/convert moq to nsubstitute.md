Here is a sample to convert Moq into NSubstitute. 

Using Moq:
```csharp
var mockService = new Mock<IService>();
mockService.Setup(s => s.Method()).Returns(result);
mockService.Setup(s => s.MethodAsync()).ReturnsAsync(result);
```

Using NSubstitute:
```csharp
var mockService = Substitute.For<IService>();
mockService.Method().Returns(result);
mockService.MethodAsync().Returns(Task.FromResult(result));
```