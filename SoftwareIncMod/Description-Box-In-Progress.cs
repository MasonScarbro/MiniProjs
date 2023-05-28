using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;

namespace myMod
{
    internal class MyModMeta : ModMeta
    {
        public override void ConstructOptionsScreen(RectTransform parent, bool inGame)
        {
            Text text = WindowManager.SpawnLabel();
            text.text = "Please Select the Description Box Mod";
            WindowManager.AddElementToElement(text.gameObject, parent.gameObject, new Rect(0f, 0f, 400f, 128f),
                new Rect(0f, 0f, 0f, 0f));
        }

        public override string Name => "My Mod!";
    }

    internal class CreatesTehBox {
       public void CreateInputBoxInside(RectTransform parent, bool inGame)
        {
        GameObject neededParentPanel = WindowManager.FindElementPath("DesignDocumentWindow/ContentPanel/PageContent/InfoPanel").gameObject;
        InputField Description = WindowManager.SpawnInputbox();
        WindowManager.AddElementToElement(Description.gameObject, neededParentPanel, new Rect(0f, 0f, 400f, 128f),
            new Rect(0f, 0f, 0f, 0f));
        }

    }

}
