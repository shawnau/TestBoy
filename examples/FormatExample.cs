namespace FormatExampleNamespace
{
    using System;
    using System.Collections.Generic;

    using Microsoft.Namespace1.SomeNamespace;
    using Microsoft.Namespace2.SomeNamespace;
    using Microsoft.Namespace3.SomeNamespace;
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    /// <summary>
    /// Test class for FormatExample
    /// </summary>
    [TestClass]
    public class FormatExampleTests
    {
        /// <summary>
        /// Some Sample Constant
        /// </summary>
        internal const string SampleConstant = @"some sample constant";
        
        /// <summary>
        /// Test for the default constructor
        /// </summary>
        [TestMethod]
        public void DefaultConstructorTests()
        {
            // Act
            var example = new FormatExample();

            // Assert
            Assert.IsNull(example.Key);
            Assert.IsNull(example.Value);
        }

        /// <summary>
        /// Test for the Constructor
        /// </summary>
        [TestMethod]
        public void ConstructorTests()
        {
            // Arrange
            string key = "TestKey";
            string value = "TestValue";

            // Act
            var example = new FormatExample(key, value);

            // Assert
            Assert.AreEqual(key, example.Key);
            Assert.AreEqual(value, example.Value);
        }
    }
}
