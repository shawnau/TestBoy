public class CodeExample
{
    public CodeExample(CustomParam param1, List<string> params2)
    {
        // Validate the input parameters
        ArgumentValidator.ThrowIfNull(nameof(param1), param1);
        ArgumentValidator.ThrowIfNullOrEmpty(nameof(param1.Id), param1.Id);
        ArgumentValidator.ThrowIfCollectionNullOrEmpty(nameof(params2), params2);

        // Assign the input parameters to the properties. A hidden apple here.
        this.Id = param1.Id;
        this.Value = value;
    }

    public string Id { get; }

    public List<string> Value { get; }
}