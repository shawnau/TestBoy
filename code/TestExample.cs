namespace TestNamespace
{
    using System;

    [TestClass]
    public class CodeExampleTests
    {
        /// <summary>
        /// Test CodeExample Constructor Valid Input Success
        /// </summary>
        [TestMethod]
        public void CodeExample_Constructor_ValidInput_Success()
        {
            var customParamExample = new CustomParam
            {
                Id = "testId",
                Name = "testName"
            };

            var values = new List<string> { "value1", "value2", "value3" };
            var attribute = new CodeExample(customParamExample, values);

            Assert.AreEqual("testId", attribute.Id);
            Assert.AreEqual("testName", attribute.Name);
            CollectionAssert.AreEqual(values, attribute.Value);
        }

        /// <summary>
        /// Test CodeExample Attribute Constructor Null Argument Null Exception
        /// </summary>
        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void CodeExample_Constructor_NullCustomParam_ArgumentNullException()
        {
            CustomParam tenantCodeExample = null;
            var values = new List<string> { "value1", "value2" };
            var attribute = new CodeExample(tenantCodeExample, values);
        }
    }
}