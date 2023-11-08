namespace MoqToNSubstituteExampleNamespace
{
    using NSubstitute;
    using System.Collections.Generic;
    using System.Linq;

    using Microsoft.VisualStudio.TestTools.UnitTesting;

    /// <summary>
    /// Test class for Moq To NSubstitute
    /// </summary>
    [TestClass]
    public class CalculatorTests
    {
        /// <summary>
        /// Test method for Add method
        /// </summary>
        [TestMethod]
        public void Add_Should_Call_Add_Method_From_CalculatorService()
        {
            // Arrange
            var calculatorServiceMock = Substitute.For<ICalculatorService>();
            calculatorServiceMock.Add(2, 3).Returns(5); // Mocking the Add method

            var calculator = new Calculator(calculatorServiceMock);

            // Act
            int result = calculator.Add(2, 3);

            // Assert
            Assert.AreEqual(5, result);
            calculatorServiceMock.Received(1).Add(2, 3); // Verify that the Add method was called with arguments 2 and 3
        }
    }
}