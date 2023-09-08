sample_comment = '''/// <summary>
/// This is a sample comment
/// </summary>
'''

moq_sample = '''var mockService = new Mock<IService>();
mockService.Setup(s => s.Method()).Returns(result);
mockService.Setup(s => s.MethodAsync()).ReturnsAsync(result);'''

nsubstitute_sample = '''var mockService = Substitute.For<IService>();
mockService.Method().Returns(result);
mockService.MethodAsync().Returns(Task.FromResult(result));'''